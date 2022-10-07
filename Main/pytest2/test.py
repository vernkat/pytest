import pytest


## simple assertions

def func(x):
    return x + 1

# fail
# def test_answer():
    assert func(3) == 5

def test_answer2():
    assert func(3) == 4


## A test function that verifies an expection 

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)



## Multiplication test ideas

# two positive integers
# identity: multiplying any number by 1
# zero: multiplying any number by 0
# positive by a negative
# negative by a negative
# multiplying floats

numbers = [
    (2, 3, 6),             # positive integers
    (1, 99, 99),           # identity
    (0, 99, 0),            # zero
    (3, -4, -12),          # positive by negative
    (-5, -5, 25),          # negative by negative
    (2.5, 6.7, 16.75)      # floats
]

@pytest.mark.parametrize('a, b, number', numbers)
def test_multiplication(a, b, number):
    assert a * b == number