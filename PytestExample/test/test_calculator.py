import pytest

from src.calculator import addition, subtraction, multiplication, division


def test_addition():
    res = addition(20,10)
    assert res == 30

def test_subtraction():
    res = subtraction(20,10)
    assert res == 10

def test_multiplication():
    res = multiplication(20,10)
    assert res == 200

def test_division_posdata():
    res = division(20,10)
    assert res == 2

def test_division_negdata():
    with pytest.raises(ZeroDivisionError):
        division(20,0)