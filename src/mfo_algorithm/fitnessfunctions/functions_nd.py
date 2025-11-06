# src/mfo_algorithm/fitnessfunctions/functions_nd.py

"""
N-Dimensional Benchmark Fitness Functions
========================================
This module contains classic N-dimensional (variable dimension) benchmark functions
used for testing optimization algorithms.

Functions:
- exponential
- griewank
- powellsum
- ridge
- schwefel2_20
- schwefel2_21
- schwefel2_22
- schwefel2_23
- sphere
- sumsquares
- xinsheyangn3
- zakharov
"""

import numpy as np
from typing import List

# --- Functions ---
def sphere(x: List[float]) -> float:
    x = np.array(x)
    return np.sum(x ** 2)

def griewank(x: List[float]) -> float:
    x = np.array(x)
    sum_term = np.sum(x**2) / 4000
    prod_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x)+1))))
    return 1 + sum_term - prod_term

def powellsum(x: List[float]) -> float:
    x = np.array(x)
    return np.sum([abs(xi ** (i+2)) for i, xi in enumerate(x)])

def ridge(x: List[float]) -> float:
    x = np.array(x)
    alpha, d = 0.5, 1
    return x[0] + ((d * (np.sum(x**2) - x[0]**2)) ** alpha)

def schwefel2_20(x: List[float]) -> float:
    return np.sum(np.abs(x))

def schwefel2_21(x: List[float]) -> float:
    return np.max(np.abs(x))

def schwefel2_22(x: List[float]) -> float:
    x = np.array(x)
    return np.sum(np.abs(x)) + np.prod(np.abs(x))

def schwefel2_23(x: List[float]) -> float:
    x = np.array(x)
    return np.sum(x ** 10)

def sumsquares(x: List[float]) -> float:
    return np.sum([xi**2 * (i+1) for i, xi in enumerate(x)])

def xinsheyangn3(x: List[float]) -> float:
    x = np.array(x)
    beta, m = 15, 5
    term1 = np.exp(-np.sum((x / beta) ** (2*m)))
    term2 = -2 * np.exp(-np.sum(x**2)) * np.prod(np.cos(x)**2)
    return term1 + term2

def zakharov(x: List[float]) -> float:
    x = np.array(x)
    sum1 = np.sum(x**2)
    sum2 = np.sum([0.5 * xi * (i+1) for i, xi in enumerate(x)])
    return sum1 + sum2**2 + sum2**4

# --- Metadata ---
args = {
    "sphere": {"dim": 0, "lb": -100, "ub": 100},
    "griewank": {"dim": 0, "lb": -600, "ub": 600},
    "powellsum": {"dim": 0, "lb": -10, "ub": 10},
    "ridge": {"dim": 0, "lb": -5, "ub": 5},
    "schwefel2_20": {"dim": 0, "lb": -100, "ub": 100},
    "schwefel2_21": {"dim": 0, "lb": -100, "ub": 100},
    "schwefel2_22": {"dim": 0, "lb": -10, "ub": 10},
    "schwefel2_23": {"dim": 0, "lb": -1, "ub": 1},
    "sumsquares": {"dim": 0, "lb": -10, "ub": 10},
    "xinsheyangn3": {"dim": 0, "lb": -5, "ub": 5},
    "zakharov": {"dim": 0, "lb": -5, "ub": 10},
}
