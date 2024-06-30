def addition(x: int, y: int) -> int:
    """addition

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: int
    """
    return x + y

def multiplication(x: int, y: int) -> int:
    """multiplication

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: int
    """
    return x * y

def division(x, y):
    """division

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: int
    """
    return x / y

def subtraction(x, y):
    """subtraction

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: int
    """
    return x - y

if __name__ == "__main__":
    print(f"Result is: {addition(100, 100)}")
