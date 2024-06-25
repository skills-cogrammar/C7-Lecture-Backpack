# Python Fibonacci Code
def fibonacci(n):
    if n <= 1:
        return n  # T0 = 0, T1 = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

