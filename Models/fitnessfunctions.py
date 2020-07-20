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

            scores = (
                (value[0] ** 2) +\
                    (2 * (value[1] ** 2)) -\
                    (0.3 * np.cos(3 *\
                    np.pi* value[0])) -\
                    (0.4 * np.cos(4 * np.pi * value[1])) + (0.7)
            )
        
            return scores

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