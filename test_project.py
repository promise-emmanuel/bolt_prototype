from project import calculate, calculate1
import pytest
from pytest import approx

def test_calculate():
    '''verify that the calculate function works correctly
    '''

    assert calculate(1134) == approx(113.4, 0.1)
    assert calculate(1000) == approx(100) 

def test_calculate1():
    '''verify that the calculate1 function works correctly
    '''

    assert calculate1(1134) == approx(226.8, 0.1)
    assert calculate1(1000) == approx(200) 


pytest.main(["-v", "--tb=line", "-rN", __file__])