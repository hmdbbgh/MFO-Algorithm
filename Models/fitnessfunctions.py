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