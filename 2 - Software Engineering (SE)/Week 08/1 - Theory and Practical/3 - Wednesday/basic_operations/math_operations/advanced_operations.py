# advanced_operations.py

def power(x, y):
    return x ** y

def square_root(x):
    return x ** 0.5

def absolute_value(x):
    return abs(x)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
