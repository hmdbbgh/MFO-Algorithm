import sys

import random

import numpy as np

import pandas as pd

import matplotlib.pyplot as plot   

from Models.fitnessfunctions import FitnessFunctions


class MFO:


    def __init__(self,
                 max_iteration, number_of_moths, fitnessfunction,
                 initialized_automatically = True, dimension = 0, *args, **kwargs):

        self.dimension = dimension
        
        self.max_iteration = max_iteration

        self.number_of_moths = number_of_moths

        self.fitnessfunction_name = fitnessfunction

        self.initialized_automatically = initialized_automatically

        self.is_valid()


    def is_valid(self):

        if not isinstance(self.fitnessfunction_name, str):

            sys.exit("fitnessfunction must be string")

        if not isinstance(self.dimension, int):

            sys.exit("dimension must be integer")

        if not isinstance(self.max_iteration, int):

            sys.exit("max_iteration must be integer")

        if not isinstance(self.number_of_moths, int):

            sys.exit("number_of_moths must be integer")

        if not isinstance(self.initialized_automatically, bool):

            sys.exit("initialized_automatically must be boolean")


    def get_fitnessfunction(self):

        FitnessFunctions_object = FitnessFunctions()

        fitnessfunction_args, self.fitnessfunction = FitnessFunctions_object.get(self.fitnessfunction_name)
        
        self.dimension = fitnessfunction_args['dim'] if fitnessfunction_args['dim'] else self.dimension
        
        self.lower_bound = fitnessfunction_args['lb']

        self.upper_bound = fitnessfunction_args['ub']

        if not isinstance(self.lower_bound, list):

            self.lower_bound = [self.lower_bound for i in range(self.dimension)]

        if not isinstance(self.upper_bound, list):

            self.upper_bound = [self.upper_bound for i in range(self.dimension)]

    
    def determine_the_initial_position_of_the_moths(self):

        self.position_of_moths = np.zeros((self.number_of_moths, self.dimension))

        for i in range(self.dimension):

            self.position_of_moths[:,i] = (
                                np.random.uniform(0, 1, self.number_of_moths) *\
                                (self.upper_bound[i] - self.lower_bound[i]) +\
                                self.lower_bound[i]
                            )

        self.initial_position_of_moths = self.position_of_moths

    
    def determine_the_initial_value_of_the_moths(self):

        self.fitness_of_moths = np.full(self.number_of_moths, float("inf"))


    def sort_the_first_fitness_of_moths(self):

        self.fitness_sorted = np.sort(self.fitness_of_moths)

        I = np.argsort(self.fitness_of_moths)
      
        self.sorted_population = self.position_of_moths[I,:]

    
    def determine_the_number_of_flames(self, iteration):

        return round(self.number_of_moths - iteration * ((self.number_of_moths-1) / self.max_iteration))


    def update_the_position_of_moths(self, iteration):

        number_of_flames = self.determine_the_number_of_flames(iteration)

        a = -1 + iteration * ((-1) / self.max_iteration) # a linearly dicreases in range [-2, -1] to calculate t in Eq. (3.12)

        for i in range(0, self.number_of_moths):
            
            for j in range(0, self.dimension):

                distance_to_flame = abs(
                    self.sorted_population[i,j] - self.position_of_moths[i,j]
                )  # D in Eq. (3.13)

                r = 1

                t = (a - 1) * random.random() + 1

                if i <= number_of_flames: # Update the position of the moth with respect to its corresponding flame
             
                    #Eq. (3.12)
                    self.position_of_moths[i,j] = (
                                                distance_to_flame *\
                                                np.exp(r * t) *\
                                                np.cos(t * 2 * np.pi) +\
                                                self.sorted_population[i,j]
                                            )
                       
                if i > number_of_flames: # Update the position of the moth with respect to one flame
                    
                    #Eq. (3.12)
                    self.position_of_moths[i,j] = (
                                                distance_to_flame *\
                                                np.exp(r * t) *\
                                                np.cos(t*2*np.pi) +\
                                                self.sorted_population[number_of_flames,j]
                                            )

    
    def update_the_fitness_of_flames(self, iteration, moths_family_sorted):

        if iteration == 1:

            self.sort_the_first_fitness_of_moths()

        else:
            
            moths_family = np.concatenate(
                            (self.parent_moths, self.best_flames),
                            axis = 0
                        )

            fitness_of_moths_family = np.concatenate(
                            (self.fitness_of_parent_moths, self.fitness_of_best_flames),
                            axis = 0
                        )

            fitness_of_moths_family_sorted = np.sort(fitness_of_moths_family)   
            
            I2 = np.argsort(fitness_of_moths_family)

            for newindex in range(0, 2 * self.number_of_moths):

                moths_family_sorted[newindex,:] = np.array(moths_family[I2[newindex],:])  
            
            self.fitness_sorted = fitness_of_moths_family_sorted[0:self.number_of_moths]
            
            self.sorted_population = moths_family_sorted[0:self.number_of_moths, :]


    def determine_the_best_flames(self):
            
        self.best_flames = self.sorted_population

        self.fitness_of_best_flames = self.fitness_sorted

    
    def valid_the_position_of_moths_to_search_space(self):
        
        for i in range(self.number_of_moths):
        
            for j in range(self.dimension):

                self.position_of_moths[i,j] = np.clip(
                                            self.position_of_moths[i,j],
                                            self.lower_bound[j],
                                            self.upper_bound[j]
                                        )


    def evaluate_the_moths(self):

        for i in range(self.number_of_moths): self.fitness_of_moths[i] = self.fitnessfunction(self.position_of_moths[i,:])

    
    def start(self):

        self.get_fitnessfunction()
        
        self.determine_the_initial_position_of_the_moths()

        self.determine_the_initial_value_of_the_moths()

        self.convergence_curve = np.zeros(self.max_iteration)

        moths_family_sorted = np.zeros((2 * self.number_of_moths, self.dimension))

        self.report = list()

        iteration = 1

        while not iteration > self.max_iteration:

            self.parent_moths = self.position_of_moths

            self.fitness_of_parent_moths = self.fitness_of_moths

            self.valid_the_position_of_moths_to_search_space()

            self.evaluate_the_moths()

            self.update_the_fitness_of_flames(iteration, moths_family_sorted)

            self.determine_the_best_flames()

            self.update_the_position_of_moths(iteration)

            self.convergence_curve[iteration - 1] = self.fitness_sorted[0]

            temp = [self.fitness_sorted[0]]

            for position in self.sorted_population[0]:

                temp.append(position)
            
            self.report.append(temp)

            iteration += 1

    def draw_the_plot(self, plot_file_path, plot_file_name):

        # Data for plotting
        plot.plot(np.arange(1, self.max_iteration + 1), self.convergence_curve)

        plot.xlabel('Iteration') 

        plot.ylabel('Cost') 

        plot.title('Fitness Function Values in Iterations') 
        
        plot.savefig('{}/{}.png'.format(plot_file_path, plot_file_name))

        # plot.show()

    
    def get_report(self):

        self.header = ['Score',]

        self.header.extend(range(self.dimension))

        # df = pd.DataFrame(self.report, index = range(1, self.max_iteration+1), columns = self.header)

        # print(df)