"""
MFO Algorithm Package
====================

This package provides implementation of the Moth-Flame Optimization (MFO) algorithm.
It contains:

- mfo.py: The main optimizer class.
- fitnessfunctions: Modules containing benchmark fitness functions for testing.

Example usage:
--------------
from mfo_algorithm.mfo import MFO

mfo = MFO(max_iteration=50, number_of_moths=30, fitnessfunction="sphere")
mfo.start()
header, report = mfo.get_report()
"""

from .mfo import MFO
