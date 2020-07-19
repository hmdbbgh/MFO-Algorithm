import sys

import numpy as np

from fitnessfunctions import FitnessFunctions


class MFO:


    def __init__(self,
                 max_iteration, number_of_moths, fitnessfunction,
                 initialized_automatically = True, *args, **kwargs):

        self.max_iteration = max_iteration

        self.number_of_moths = number_of_moths

        self.fitnessfunction_name = fitnessfunction

        self.initialized_automatically = initialized_automatically

        self.is_valid()

        self.get_fitnessfunction()
        
        self.determine_the_initial_position_of_the_moths()

        self.determine_the_initial_value_of_the_moths()


    def is_valid(self):

        if not isinstance(self.fitnessfunction_name, str):

            sys.exit("fitnessfunction must be string")

        if not isinstance(self.max_iteration, int):

            sys.exit("max_iteration must be integer")

        if not isinstance(self.number_of_moths, int):

            sys.exit("number_of_moths must be integer")

        if not isinstance(self.initialized_automatically, bool):

            sys.exit("initialized_automatically must be boolean")


    def get_fitnessfunction(self):

        FitnessFunctions_object = FitnessFunctions()

        fitnessfunction_args, self.fitnessfunction = FitnessFunctions_object.get(self.fitnessfunction_name)

        self.dimension = fitnessfunction_args['dim']

        self.lower_bound = fitnessfunction_args['lb']

        self.upper_bound = fitnessfunction_args['ub']

        print(self.fitnessfunction(np.array([1,2,4,4])))

        if not isinstance(self.lower_bound, list):

            self.lower_bound = [self.lower_bound for i in range(self.dimension)]

        if not isinstance(self.upper_bound, list):

            self.upper_bound = [self.upper_bound for i in range(self.dimension)]

        print(self.dimension, self.lower_bound, self.upper_bound)

    
    def determine_the_initial_position_of_the_moths(self):

        self.position_of_moths = np.zeros((self.number_of_moths, self.dimension))

        print(self.position_of_moths)

        for i in range(10):

            self.position_of_moths[:,i] = np.random.uniform(0, 1, self.number_of_moths) *\
                                     (self.upper_bound[i] - self.lower_bound[i]) + self.lower_bound[i]

        print(self.position_of_moths)

    
    def determine_the_initial_value_of_the_moths(self):

        self.fitness_of_moths = np.full(self.number_of_moths, float("inf"))

        print(self.fitness_of_moths)

    
    def determine_the_number_of_flames(self, iteration):

        return round(self.number_of_moths - iteration * ((self.number_of_moths-1) / self.max_iteration))

    
    def valid_the_position_of_moths_to_search_space(self):
        
        for i in range(self.number_of_moths):
        
            for j in range(self.dimension):

                self.position_of_moths[i,j] = np.clip(self.position_of_moths[i,j], self.lower_bound[j], self.upper_bound[j])


    def evaluate_the_moths(self):

        for i in range(self.number_of_moths): self.fitness_of_moths[i] = self.fitnessfunction(self.position_of_moths[i,:])

        print(self.fitness_of_moths)

    
    
        


a = MFO(10,10,'sphere')

# a.determine_the_initial_position_of_the_moths()

# a.determine_the_number_of_flames(1)

# a.evaluate_the_moths()
# a.get_fitnessfunction()

