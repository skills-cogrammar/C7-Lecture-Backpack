from calc_app import addition, subtraction, multiplication, division

def test_add():
    assert addition(5, 5) == 10

def test_add_zero():
    assert addition(0, 0) == 0

def test_division():
    assert division(5, 5) == 1

def test_subtraction():
    assert subtraction(5, 5) == 0

def test_subtraction_zero():
    assert subtraction(0, 0) == 0

def test_multiplication():
    assert multiplication(5, 5) == 25