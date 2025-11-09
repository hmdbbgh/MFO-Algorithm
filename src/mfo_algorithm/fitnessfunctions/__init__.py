# src/mfo_algorithm/fitnessfunctions/__init__.py
from .functions_2d import *
from .functions_nd import *
import sys

class FitnessFunctions:
    """
    Wrapper class to handle fitness functions
    """
    def get_functions_name(self):
        return self.args('all')

    def get_n_dimension_functions_name(self):
        return self.args("n_dimension")

    def get(self, name):
        try:
            return self.args(name), getattr(self, name)
        except AttributeError:
            sys.exit(f'There is no function named "{name}"')

    def args(self, name):
        """
        Returns metadata for fitness functions: dim, lb, ub
        """
        from .functions_2d import args as args_2d
        from .functions_nd import args as args_nd
        args = {**args_2d, **args_nd}

        if name == 'all':
            return list(args.keys())
        if name == 'n_dimension':
            return list(filter(lambda key: args[key]['dim'] == 0, args.keys()))
        details = args.get(name)
        if details:
            return {'dim': details['dim'], 'lb': details['lb'], 'ub': details['ub']}
        else:
            sys.exit(f'There is no function named "{name}"\'s details')
