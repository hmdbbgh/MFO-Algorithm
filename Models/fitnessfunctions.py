import sys

import numpy as np


class FitnessFunctions:


    def get(self, name):
        
        try:

            return self.args(name), getattr(self, name)

        except AttributeError:

            sys.exit('There is no function named "{}"'.format(name))

    
    def args(self, name):           # dim == dimension, lb == lower bound, ub == upper bound

        args = {
            # 'function_name': {
            #   'dim': value,
            #   'lb': value,
            #   'ub': value
            # }

            'ackleyn2': {
                'dim': 2,
                'lb': -32,
                'ub': 32
            },

            'bohachevskyn1': {
                'dim': 2,
                'lb': -100,
                'ub': 100
            },

            'booth': {
                'dim': 2,
                'lb': -10,
                'ub': 10
            },

            'brent': {
                'dim': 2,
                'lb': -20,
                'ub': 0
            },

            'brown': {
                'dim': 0,
                'lb': -1,
                'ub': 4
            },

            'dropwave': {
                'dim': 2,
                'lb': -5.2,
                'ub': 5.2
            },

            'exponential': {
                'dim': 0,
                'lb': -1,
                'ub': 1
            }, 

            'griewank': {
                'dim': 0,
                'lb': -600,
                'ub': 600
            }, 

            'leon': {
                'dim': 2,
                'lb': 0,
                'ub': 10
            },

            'matyas': {
                'dim': 2,
                'lb': -10,
                'ub': 10
            },

            'sphere': {
                'dim': 10,
                'lb': -5.12,
                'ub': 5.12
            },              
        }

        details = args.get(name)

        if details:

            result = {
                'dim': details['dim'],
                'lb': details['lb'],
                'ub': details['ub']
            }
        
            return result

        else:

            sys.exit('There is no function named "{}"\'s details'.format(name))
            
    
    def ackleyn2(self, value):

        if len(value) == 2:

            return (-200) * (np.exp((-0.2)*(np.sqrt(value[0]**2 + value[1]**2))))

        else:

            sys.exit('The Ackley N. 2 function is only defined on a 2D space.')

    
    def bohachevskyn1(self, value):

        if len(value) == 2:

            score = (
                (value[0] ** 2) +\
                    (2 * (value[1] ** 2)) -\
                    (0.3 * np.cos(3 *\
                    np.pi* value[0])) -\
                    (0.4 * np.cos(4 * np.pi * value[1])) + (0.7)
            )
        
            return score

        else:

            sys.exit('The Bohachevsky N. 1 function is only defined on a 2D space.')


    def booth(self, value):
        
        if len(value) == 2:

            score = (
                ((value[0] +\
                2 * value[1] - 7) ** 2) +\
                ((2 * value[0] + value[1] - 5) ** 2)
            )
        
            return score

        else:

            sys.exit('The Booth function is only defined on a 2D space.')

    
    def brent(self, value):

        if len(value) == 2:

            score = (
                ((value[0] + 10) ** 2) +\
                ((value[1] + 10) ** 2) +\
                np.exp(-(value[0] ** 2 +\
                value[1] ** 2))
            )
        
            return score

        else:

            sys.exit('The Brent function is only defined on a 2D space.')

    
    def brown(self, value):

        score = 0

        for i in range(len(value) - 1):

            score += (
                ((value[i] ** 2) ** ((value[i+1] ** 2) + 1)) +\
                ((value[i+1] ** 2) ** ((value[i] ** 2) + 1))
            )

        return score

    
    def dropwave(self, value):
    
        if len(value) == 2:

            score = -(
                (1 + (np.cos(12 * np.sqrt(value[0] ** 2 + value[1] ** 2)))) /\
                ((0.5 * (value[0] ** 2 + value[1] ** 2)) + 2)
            )
            
            return score

        else:

            sys.exit('The Drop-Wave function is only defined on a 2D space.')


    def exponential(self, value):
    
        return -np.exp((-0.5) * (np.sum(value ** 2)))

    
    def griewank(self, value):

        score = (
            1 +\
            ((1 / 4000) *\
            np.sum(value)) +\
            np.prod(list(
                        map(
                            lambda x: np.cos(x[0]/np.sqrt(x[1])), zip(value, range(1, len(value)+1))
                            )
                        )
                    )
        )

        return score

    
    def leon(self, value):

        if len(value) == 2:

            return (100 * (value[1] - value[0] ** 3) ** 2) + ((1 - value[0]) ** 2)

        else:

            sys.exit('The Leon function is only defined on a 2D space.')
    
    
    def matyas(self, value):

        if len(value) == 2:

            return (0.26 * (value[0] ** 2 + value[1] ** 2)) - (0.48 * value[0] * value[1])

        else:

            sys.exit('The Matyas function is only defined on a 2D space.')
    

    def sphere(self, value):
        
        return np.sum(value**2)