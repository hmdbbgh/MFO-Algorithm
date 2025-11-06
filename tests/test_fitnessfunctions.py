import pytest
from mfo_algorithm.fitnessfunctions import FitnessFunctions
import numpy as np

def test_sphere_function():
    ff = FitnessFunctions()
    f = ff.get("sphere")[1]
    val = np.array([1,2,3])
    assert f(val) == sum(val**2)

def test_2d_function():
    ff = FitnessFunctions()
    f = ff.get("booth")[1]
    val = np.array([1,3])
    expected = ((1 + 2*3 - 7)**2) + ((2*1 + 3 - 5)**2)
    assert f(val) == expected
