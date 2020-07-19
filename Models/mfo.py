import sys

import numpy as np


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

        # get dimension and upper bound and lower bound

        self.dimension = 10

        self.lower_bound = -5.12

        self.upper_bound = 5.12

        if not isinstance(self.lower_bound, list):

            self.lower_bound = [self.lower_bound for i in range(self.dimension)]

        if not isinstance(self.upper_bound, list):

            self.upper_bound = [self.upper_bound for i in range(self.dimension)] 

    
    def determine_the_initial_position_of_the_moths(self):

        self.position_of_moths = np.zeros((self.number_of_moths, self.dimension))

        print(self.position_of_moths)

        for i in range(10):

            self.position_of_moths[:,i] = np.random.uniform(0, 1, self.number_of_moths) *\
                                     (self.upper_bound[i] - self.lower_bound[i]) + self.lower_bound[i]

        print(self.position_of_moths)

        self.determine_the_initial_value_of_the_moths()

    
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

        for i in range(self.number_of_moths): self.fitness_of_moths[i] = self.sphere(self.position_of_moths[i,:])

        print(self.fitness_of_moths)

    
    def sphere(self, x):
        
        return np.sum(x**2)
        


a = MFO(10,10,'a')

a.determine_the_initial_position_of_the_moths()

a.determine_the_number_of_flames(1)

a.evaluate_the_moths()