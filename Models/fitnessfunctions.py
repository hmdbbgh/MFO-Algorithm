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

            'powellsum': {
                'dim': 0,
                'lb': -1,
                'ub': 1
            },

            'ridge': {
                'dim': 0,
                'lb': -5,
                'ub': 5
            }, 

            'schaffern1': {
                'dim': 2,
                'lb': -100,
                'ub': 100
            }, 

            'schaffern2': {
                'dim': 2,
                'lb': -100,
                'ub': 100
            }, 

            'schaffern3': {
                'dim': 2,
                'lb': -100,
                'ub': 100
            }, 

            'schwefel2_20': {
                'dim': 0,
                'lb': -100,
                'ub': 100
            }, 

            'schwefel2_21': {
                'dim': 0,
                'lb': -100,
                'ub': 100
            }, 

            'schwefel2_22': {
                'dim': 0,
                'lb': -100,
                'ub': 100
            }, 

            'schwefel2_23': {
                'dim': 0,
                'lb': -10,
                'ub': 10
            }, 

            'sphere': {
                'dim': 0,
                'lb': -5.12,
                'ub': 5.12
            },   

            'sumsquares': {
                'dim': 0,
                'lb': -10,
                'ub': 10
            },    
                      
            'threehumpcamel': {
                'dim': 2,
                'lb': -5,
                'ub': 5
            },       

            'xinsheyangn3': {
                'dim': 0,
                'lb': -2 * np.pi,
                'ub': 2 * np.pi
            },              

            'zakharov': {
                'dim': 0,
                'lb': -5,
                'ub': 10
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
        import pdb ; pdb.set_trace()
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

    
    def powellsum(self, value):

        score = (
            np.sum(list(
                        map(
                            lambda x: abs(x[0] ** x[1]), zip(value, range(2, len(value)+2))
                            )
                        )
                )
        )

        return score

    
    def ridge(self, value):

        alpha, d = 0.5, 1
        
        return value[0] + ((d * (np.sum(value ** 2) - (value[0] ** 2))) ** alpha)

    
    def schaffern1(self, value):
        
        if len(value) == 2:

            score = (
                0.5 +\
                (
                    ((np.sin(value[0] ** 2 + value[1] ** 2) ** 2) - (0.5)) /\
                    (((1) + (0.001 * (value[0] ** 2 + value[1] ** 2))) ** 2)
                )
            )

            return score

        else:

            sys.exit('The Schaffer N. 1 function is only defined on a 2D space.')


    def schaffern2(self, value):
        
        if len(value) == 2:

            score = (
                0.5 +\
                (
                    ((np.sin(value[0] ** 2 - value[1] ** 2)) - (0.5)) /\
                    (((1) + (0.001 * (value[0] ** 2 + value[1] ** 2))) ** 2)
                )
            )

            return score

        else:

            sys.exit('The Schaffer N. 2 function is only defined on a 2D space.')


    def schaffern3(self, value):
        
        if len(value) == 2:

            score = (
                0.5 +\
                (
                    ((np.sin(np.cos(abs(value[0] ** 2 - value[1] ** 2))) ** 2) - (0.5)) /\
                    (((1) + (0.001 * (value[0] ** 2 + value[1] ** 2))) ** 2)
                )
            )

            return score

        else:

            sys.exit('The Schaffer N. 3 function is only defined on a 2D space.')


    def schaffern4(self, value):
        
        if len(value) == 2:

            score = (
                0.5 +\
                (
                    ((np.cos(np.sin(abs(value[0] ** 2 - value[1] ** 2))) ** 2) - (0.5)) /\
                    (((1) + (0.001 * (value[0] ** 2 + value[1] ** 2))) ** 2)
                )
            )

            return score

        else:

            sys.exit('The Schaffer N. 4 function is only defined on a 2D space.')

    
    def schwefel2_20(self, value):
    
        return np.sum(abs(value))

    
    def schwefel2_21(self, value):
    
        return np.max(abs(value))

    
    def schwefel2_22(self, value):
    
        return np.sum(abs(value)) + np.prod(abs(value))

    
    def schwefel2_23(self, value):
    
        return np.sum(value ** 10)


    def sphere(self, value):
        
        return np.sum(value ** 2)


    def sumsquares(self, value):

        score = (
                np.sum(list(
                            map(
                                lambda x: ((x[0]**2) * x[1]), zip(value, range(1, len(value)+1))
                                )
                            )
                    )
            )

        return score

    
    def threehumpcamel(self, value):
    
        score =  (
            (2 * (value[0] ** 2)) -\
            (1.05 * (value[0] ** 4)) +\
            ((value[0] ** 6) / 6) +\
            (value[0] * value[1]) +\
            (value[1] ** 2)
        )
        
        return score

    
    def xinsheyangn3(self, value):

        beta, m = 15, 5

        score = (
            np.exp(-np.sum((value / beta) ** (2 * m))) +\
            (
                (-2 * np.exp(-np.sum(value ** 2))) *\
                np.prod(np.cos(value) ** 2)
            )
        )

        return score

    
    def zakharov(self, value):

        score = (
                np.sum(value ** 2) +\
                ((np.sum(list(
                            map(
                                lambda x: (0.5 * x[0] * x[1]), zip(value, range(1, len(value)+1))
                                )
                            )
                    )) ** 2) +\
                ((np.sum(list(
                            map(
                                lambda x: (0.5 * x[0] * x[1]), zip(value, range(1, len(value)+1))
                                )
                            )
                    )) ** 4)
            )

        return score