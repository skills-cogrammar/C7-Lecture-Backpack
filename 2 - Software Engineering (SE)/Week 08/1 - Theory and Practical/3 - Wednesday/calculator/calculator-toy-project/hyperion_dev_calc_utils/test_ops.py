from ops import add, subtract, multiply, divide

# Positive tests
def test_add_positive():
    """Test cases for the add function."""
    assert add(5, 3) == 8
    assert add(0, 0) == 0
    assert add(-5, 3) == -2

def test_subtract_positive():
    """Test cases for the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-5, -3) == -2

def test_multiply_positive():
    """Test cases for the multiply function."""
    assert multiply(5, 3) == 15
    assert multiply(0, 5) == 0
    assert multiply(-5, -3) == 15

def test_divide_positive():
    """Test cases for the divide function."""
    assert divide(10, 2) == 5
    assert divide(0, 5) == 0
    assert divide(-10, -2) == 5

# Negative tests
def test_divide_by_zero():
    """Test case for division by zero."""
    assert divide(10, 0) == "Error"