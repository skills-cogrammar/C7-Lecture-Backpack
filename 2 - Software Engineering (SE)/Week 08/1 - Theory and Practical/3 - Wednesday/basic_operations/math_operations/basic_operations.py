# basic_operations.py

__all__ = ["addition", "subtraction", "division", "multiplication"]

def addition(x, y):
    return _addition(x, y)

def subtraction(x, y):
    return _subtraction(x, y)

def division(x, y):
    return _division(x, y)

def multiplication(x, y):
    return _multiplication(x, y)


def _addition(x, y):
    return x + y

def _subtraction(x, y):
    return x - y

def _division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def _multiplication(x, y):
    return x * y











