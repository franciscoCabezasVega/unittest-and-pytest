import pytest
from src.calculator import add, subtract, multiply, divide, power

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 5, -5),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.parametrize("base,exponent,expected", [
    (2, 3, 8),
    (5, 0, 1),
    (9, 0.5, 3),
])
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected
