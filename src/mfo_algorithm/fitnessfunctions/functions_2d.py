# src/mfo_algorithm/fitnessfunctions/functions_2d.py

"""
2D Benchmark Fitness Functions
==============================
This module contains classic 2D benchmark functions used for testing optimization algorithms.

Functions:
- ackleyn2
- bohachevskyn1
- booth
- brent
- brown
- dropwave
- leon
- matyas
- schaffern1
- schaffern2
- schaffern3
- schaffern4
"""


import sys
import numpy as np
from typing import List

# --- Functions ---
def ackleyn2(x: List[float]) -> float:
    """Ackley function in 2D"""
    if len(x) != 2:
        sys.exit('Ackley N.2 function is only defined in 2D space.')
    return -200 * np.exp(-0.2 * np.sqrt(x[0]**2 + x[1]**2))

def bohachevskyn1(x: List[float]) -> float:
    """Bohachevsky N.1 function in 2D"""
    if len(x) != 2:
        sys.exit('Bohachevsky N.1 function is only defined in 2D space.')
    return (x[0]**2 + 2*x[1]**2 - 0.3*np.cos(3*np.pi*x[0]) - 0.4*np.cos(4*np.pi*x[1]) + 0.7)

def booth(x: List[float]) -> float:
    """Booth function in 2D"""
    if len(x) != 2:
        sys.exit('Booth function is only defined in 2D space.')
    return ((x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2)

def brent(x: List[float]) -> float:
    """Brent function in 2D"""
    if len(x) != 2:
        sys.exit('Brent function is only defined in 2D space.')
    return (x[0]+10)**2 + (x[1]+10)**2 + np.exp(-(x[0]**2 + x[1]**2))

def brown(x: List[float]) -> float:
    """Brown function in 2D"""
    score = 0
    for i in range(len(x)-1):
        score += ((x[i]**2)**(x[i+1]**2 + 1)) + ((x[i+1]**2)**(x[i]**2 + 1))
    return score

def dropwave(x: List[float]) -> float:
    """Drop-Wave function in 2D"""
    if len(x) != 2:
        sys.exit('Drop-Wave function is only defined in 2D space.')
    return -(1 + np.cos(12 * np.sqrt(x[0]**2 + x[1]**2))) / (0.5*(x[0]**2 + x[1]**2) + 2)

def leon(x: List[float]) -> float:
    """Leon function in 2D"""
    if len(x) != 2:
        sys.exit('Leon function is only defined in 2D space.')
    return 100*(x[1]-x[0]**3)**2 + (1-x[0])**2

def matyas(x: List[float]) -> float:
    """Matyas function in 2D"""
    if len(x) != 2:
        sys.exit('Matyas function is only defined in 2D space.')
    return 0.26*(x[0]**2 + x[1]**2) - 0.48*x[0]*x[1]

def schaffern1(x: List[float]) -> float:
    """Schaffer N.1 function in 2D"""
    if len(x) != 2:
        sys.exit('Schaffer N.1 function is only defined in 2D space.')
    return 0.5 + ((np.sin(x[0]**2 + x[1]**2)**2 - 0.5) / (1 + 0.001*(x[0]**2 + x[1]**2))**2)

def schaffern2(x: List[float]) -> float:
    """Schaffer N.2 function in 2D"""
    if len(x) != 2:
        sys.exit('Schaffer N.2 function is only defined in 2D space.')
    return 0.5 + ((np.sin(x[0]**2 - x[1]**2) - 0.5) / (1 + 0.001*(x[0]**2 + x[1]**2))**2)

def schaffern3(x: List[float]) -> float:
    """Schaffer N.3 function in 2D"""
    if len(x) != 2:
        sys.exit('Schaffer N.3 function is only defined in 2D space.')
    return 0.5 + ((np.sin(np.cos(abs(x[0]**2 - x[1]**2)))**2 - 0.5) / (1 + 0.001*(x[0]**2 + x[1]**2))**2)

def schaffern4(x: List[float]) -> float:
    """Schaffer N.4 function in 2D"""
    if len(x) != 2:
        sys.exit('Schaffer N.4 function is only defined in 2D space.')
    return 0.5 + ((np.cos(np.sin(abs(x[0]**2 - x[1]**2)))**2 - 0.5) / (1 + 0.001*(x[0]**2 + x[1]**2))**2)

# --- Metadata ---
args = {
    "ackleyn2": {"dim": 2, "lb": -32, "ub": 32},
    "booth": {"dim": 2, "lb": -10, "ub": 10},
    "brent": {"dim": 2, "lb": -10, "ub": 10},
    "brown": {"dim": 2, "lb": -1, "ub": 4},
    "dropwave": {"dim": 2, "lb": -1, "ub": 1},
    "leon": {"dim": 2, "lb": -1.5, "ub": 1.5},
    "matyas": {"dim": 2, "lb": -10, "ub": 10},
    "schaffern1": {"dim": 2, "lb": -100, "ub": 100},
    "schaffern2": {"dim": 2, "lb": -100, "ub": 100},
    "schaffern3": {"dim": 2, "lb": -100, "ub": 100},
    "schaffern4": {"dim": 2, "lb": -100, "ub": 100},
    "bohachevskyn1": {"dim": 2, "lb": -100, "ub": 100},
}
