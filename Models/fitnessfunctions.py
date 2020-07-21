import sys

import numpy as np


class FitnessFunctions:

    
    def __init__(self, *args, **kwargs):
    
        pass


    def get(self, name):
        
        try:

            return getattr(self, name+'_args')(), getattr(self, name)

        except AttributeError:

            sys.exit('There is no function named "{}"'.format(name))


    def get_args(self, name):
        
        try:

            return getattr(self, name+'_args')()

        except AttributeError:

            sys.exit('There is no function named "{}"'.format(name))

    
    def ackleyn2(self, value):

        if len(value) == 2:

            return (-200) * (np.exp((-0.2)*(np.sqrt(value[0]**2 + value[1]**2))))

        else:

            sys.exit('The Ackley N. 2 function is only defined on a 2D space.')

    
    def ackleyn2_args(self):

        dimension, lower_bound, upper_bound = 2, -32, 32

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result

    
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


    def bohachevskyn1_args(self):

        dimension, lower_bound, upper_bound = 2, -100, 100

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result


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


    def booth_args(self):

        dimension, lower_bound, upper_bound = 2, -10, 10

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result

    
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

    
    def brent_args(self):

        dimension, lower_bound, upper_bound = 2, -20, 0

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result

    
    def brown(self, value):

        score = 0

        for i in range(len(value) - 1):

            score += (
                ((value[i] ** 2) ** ((value[i+1] ** 2) + 1)) +\
                ((value[i+1] ** 2) ** ((value[i] ** 2) + 1))
            )

        return score

    
    def brown_args(self):

        dimension, lower_bound, upper_bound = 0, -1, 4

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result

    
    def dropwave(self, value):
    
        if len(value) == 2:

            score = -(
                (1 + (np.cos(12 * np.sqrt(value[0] ** 2 + value[1] ** 2)))) /\
                ((0.5 * (value[0] ** 2 + value[1] ** 2)) + 2)
            )
            
            return score

        else:

            sys.exit('The Drop-Wave function is only defined on a 2D space.')

    
    def dropwave_args(self):

        dimension, lower_bound, upper_bound = 2, -5.2, 5.2

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result


    def exponential(self, value):
    
        return -np.exp((-0.5) * (np.sum(value ** 2)))

    
    def exponential_args(self):

        dimension, lower_bound, upper_bound = 0, -1, 1

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result

    
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

    
    def griewank_args(self):

        dimension, lower_bound, upper_bound = 0, -600, 600

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result

    
    def leon(self, value):

        if len(value) == 2:

            return (100 * (value[1] - value[0] ** 3) ** 2) + ((1 - value[0]) ** 2)

        else:

            sys.exit('The Leon function is only defined on a 2D space.')
    

    def leon_args(self):

        dimension, lower_bound, upper_bound = 2, 0, 10

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result

    
    def matyas(self, value):

        if len(value) == 2:

            return (0.26 * (value[0] ** 2 + value[1] ** 2)) - (0.48 * value[0] * value[1])

        else:

            sys.exit('The Matyas function is only defined on a 2D space.')
    
        
    def matyas_args(self):

        dimension, lower_bound, upper_bound = 2, -10, 10

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result


    def sphere(self, value):
        
        return np.sum(value**2)

    
    def sphere_args(self):

        dimension, lower_bound, upper_bound = 10, -5.12, 5.12

        result = {
            'dim': dimension,
            'lb': lower_bound,
            'ub': upper_bound
        }
        
        return result