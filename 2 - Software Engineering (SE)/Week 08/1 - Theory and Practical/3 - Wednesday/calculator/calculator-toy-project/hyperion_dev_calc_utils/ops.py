"""
File: ops.py

Description:
This file provides basic mathematical operations such as addition, subtraction, multiplication, and division. 
Each function takes two integer arguments and returns the result of the corresponding operation. 
The `add` function adds two integers, the `subtract` function subtracts one integer from another, 
the `multiply` function multiplies two integers, and the `divide` function divides one integer by 
another. The `divide` function also handles the case where the divisor is zero by returning an error message.

Functions:
- add(x: int, y: int) -> int: Adds two integers.
- subtract(x: int, y: int) -> int: Subtracts one integer from another.
- multiply(x: int, y: int) -> int: Multiplies two integers.
- divide(x: int, y: int) -> float: Divides one integer by another. Handles division by zero.
"""


def add(x: int, y: int) -> int:
    """
    Adds two integers.

    Parameters:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The sum of x and y.
    """
    return x + y

def subtract(x: int, y: int) -> int:
    """
    Subtracts one integer from another.

    Parameters:
        x (int): The integer to subtract from.
        y (int): The integer to subtract.

    Returns:
        int: The result of subtracting y from x.
    """
    return x - y

def multiply(x: int, y: int) -> int:
    """
    Multiplies two integers.

    Parameters:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The product of x and y.
    """
    return x * y

def divide(x: int, y: int) -> float:
    """
    Divides one integer by another.

    Parameters:
        x (int): The dividend.
        y (int): The divisor. Must not be zero.

    Returns:
        float: The result of dividing x by y. Returns "Error" if y is zero.
    """
    if y == 0:
        return "Error"
    return x / y

if __name__ == "__main__":
    print(add(1,2))
