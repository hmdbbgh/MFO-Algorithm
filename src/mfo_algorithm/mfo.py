# src/mfo_algorithm/mfo.py

"""
Moth-Flame Optimization (MFO) Algorithm
=======================================
This module implements the Moth-Flame Optimization algorithm for continuous
optimization problems. It is inspired by the transverse orientation of moths
in nature and their spiral flying behavior towards flames.

Classes:
- MFO: Main class to perform the optimization.
"""

import os
import sys
import random
from typing import Callable, List, Optional, Tuple
import matplotlib.pyplot as plt

import numpy as np
from .fitnessfunctions import functions_2d, functions_nd  # Import specific modules


class MFO:
    """
    Moth-Flame Optimizer

    Attributes:
        max_iteration (int): Maximum number of iterations.
        number_of_moths (int): Number of moths (population size).
        fitnessfunction_name (str): Name of the fitness function.
        initialized_automatically (bool): Whether to initialize moth positions automatically.
        dimension (int): Problem dimension.
        position_of_moths (np.ndarray): Current position of moths.
        fitness_of_moths (np.ndarray): Fitness of moths.
        best_flames (np.ndarray): Best solutions found.
        fitness_of_best_flames (np.ndarray): Fitness of best flames.
        convergence_curve (np.ndarray): Tracks best fitness over iterations.
    """

    def __init__(
        self,
        max_iteration: int,
        number_of_moths: int,
        fitnessfunction: str,
        initialized_automatically: bool = True,
        dimension: int = 0,
    ):
        self.max_iteration = max_iteration
        self.number_of_moths = number_of_moths
        self.fitnessfunction_name = fitnessfunction
        self.initialized_automatically = initialized_automatically
        self.dimension = dimension

        self._validate_inputs()

    def _validate_inputs(self):
        """Validate constructor arguments."""
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

    def _get_fitness_function(self) -> Callable:
        """Retrieve the fitness function and its parameters."""
        from .fitnessfunctions import functions_2d, functions_nd

        # Determine function from 2D or N-D modules
        if hasattr(functions_2d, self.fitnessfunction_name):
            func_module = functions_2d
        elif hasattr(functions_nd, self.fitnessfunction_name):
            func_module = functions_nd
        else:
            sys.exit(f"No function named '{self.fitnessfunction_name}' found.")

        self.fitnessfunction: Callable = getattr(func_module, self.fitnessfunction_name)

        # Set dimension and bounds
        if hasattr(func_module, "dim") and getattr(func_module, "dim") > 0:
            self.dimension = getattr(func_module, "dim")
        self.lower_bound: List[float] = getattr(func_module, "lb", [-1] * self.dimension)
        self.upper_bound: List[float] = getattr(func_module, "ub", [1] * self.dimension)

        if not isinstance(self.lower_bound, list):
            self.lower_bound = [self.lower_bound] * self.dimension
        if not isinstance(self.upper_bound, list):
            self.upper_bound = [self.upper_bound] * self.dimension

    def _initialize_moths(self):
        """Initialize moths positions and fitness values."""
        self.position_of_moths = np.zeros((self.number_of_moths, self.dimension))
        for i in range(self.dimension):
            self.position_of_moths[:, i] = (
                np.random.uniform(0, 1, self.number_of_moths)
                * (self.upper_bound[i] - self.lower_bound[i])
                + self.lower_bound[i]
            )
        self.initial_position_of_moths = self.position_of_moths.copy()
        self.fitness_of_moths = np.full(self.number_of_moths, float("inf"))

    def _sort_moths(self):
        """Sort moths by fitness."""
        I = np.argsort(self.fitness_of_moths)
        self.fitness_sorted = np.sort(self.fitness_of_moths)
        self.sorted_population = self.position_of_moths[I, :]

    def _num_flames(self, iteration: int) -> int:
        """Calculate number of flames for current iteration."""
        return round(self.number_of_moths - iteration * ((self.number_of_moths - 1) / self.max_iteration))

    def _update_positions(self, iteration: int):
        """Update positions of moths based on logarithmic spiral."""
        number_of_flames = self._num_flames(iteration)
        a = -1 + iteration * (-1 / self.max_iteration)

        for i in range(self.number_of_moths):
            for j in range(self.dimension):
                distance_to_flame = abs(self.sorted_population[i, j] - self.position_of_moths[i, j])
                b = 1
                t = (a - 1) * random.random() + 1
                if i <= number_of_flames:
                    self.position_of_moths[i, j] = (
                        distance_to_flame * np.exp(b * t) * np.cos(t * 2 * np.pi) + self.sorted_population[i, j]
                    )
                else:
                    self.position_of_moths[i, j] = (
                        distance_to_flame * np.exp(b * t) * np.cos(t * 2 * np.pi)
                        + self.sorted_population[number_of_flames, j]
                    )

    def _clip_positions(self):
        """Ensure moths remain within search space."""
        for i in range(self.number_of_moths):
            for j in range(self.dimension):
                self.position_of_moths[i, j] = np.clip(
                    self.position_of_moths[i, j], self.lower_bound[j], self.upper_bound[j]
                )

    def _evaluate_moths(self):
        """Evaluate fitness of all moths."""
        for i in range(self.number_of_moths):
            self.fitness_of_moths[i] = self.fitnessfunction(self.position_of_moths[i, :])

    def _update_flames(self, iteration: int, moths_family_sorted: np.ndarray):
        """Update best flame positions and sorted moths."""
        if iteration == 1:
            self._sort_moths()
        else:
            moths_family = np.concatenate((self.parent_moths, self.best_flames), axis=0)
            fitness_family = np.concatenate((self.fitness_of_parent_moths, self.fitness_of_best_flames), axis=0)
            I = np.argsort(fitness_family)
            sorted_family = moths_family[I, :]
            self.fitness_sorted = np.sort(fitness_family)[: self.number_of_moths]
            self.sorted_population = sorted_family[: self.number_of_moths, :]

    def _update_best_flames(self):
        """Update the best flames after evaluation."""
        self.best_flames = self.sorted_population.copy()
        self.fitness_of_best_flames = self.fitness_sorted.copy()

    def start(self):
        """Run the MFO optimization algorithm."""
        self._get_fitness_function()
        self._initialize_moths()
        self.convergence_curve = np.zeros(self.max_iteration)
        moths_family_sorted = np.zeros((2 * self.number_of_moths, self.dimension))
        self.report: List[List[float]] = []

        iteration = 1
        while iteration <= self.max_iteration:
            self.parent_moths = self.position_of_moths.copy()
            self.fitness_of_parent_moths = self.fitness_of_moths.copy()

            self._clip_positions()
            self._evaluate_moths()
            self._update_flames(iteration, moths_family_sorted)
            self._update_best_flames()
            self._update_positions(iteration)

            # Record convergence
            self.convergence_curve[iteration - 1] = self.fitness_sorted[0]

            # Record report
            temp = [self.fitness_sorted[0]] + list(self.sorted_population[0])
            self.report.append(temp)

            iteration += 1

    def get_report(self) -> Tuple[List[str], List[List[float]]]:
        """Return report headers and collected data."""
        header = ["Score"] + [f"x{i}" for i in range(1, self.dimension + 1)]
        return header, self.report

    def draw_the_plot(self, output_dir: str, file_name: str):
        """Draw convergence curve and save to file."""
        plt.figure(figsize=(8, 6))
        plt.plot(self.convergence_curve, 'b-', linewidth=2)
        plt.title(f'MFO Convergence Curve ({self.fitnessfunction_name})')
        plt.xlabel('Iteration')
        plt.ylabel('Best Fitness')
        plt.grid(True)
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, f'{file_name}.png'))
        plt.close()