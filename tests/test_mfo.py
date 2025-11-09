import pytest
from mfo_algorithm.mfo import MFO

def test_mfo_initialization():
    mfo = MFO(max_iteration=5, number_of_moths=3, fitnessfunction="sphere")
    assert mfo.max_iteration == 5
    assert mfo.number_of_moths == 3
    assert mfo.fitnessfunction_name == "sphere"

def test_mfo_start_runs():
    mfo = MFO(max_iteration=3, number_of_moths=3, fitnessfunction="sphere")
    mfo.start()
    header, report = mfo.get_report()
    assert len(report) == 3  # number of iterations
    assert len(report[0]) == mfo.dimension + 1  # score + positions
