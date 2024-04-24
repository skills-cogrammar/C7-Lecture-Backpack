# ----------- O(1) order complexity
def get_value(my_list, key):
    """
    Retrieves the value at a specified index in a list.
    
    Parameters:
        my_list (list): The list containing the values.
        key: The index of the value to retrieve.
    
    Returns:
        The value at the specified index.
    """
    return my_list[key]

print(get_value([1, 2, 3, 4, 5], 1))  # Output: 2

def add_values(num1, num2):
    """
    Adds two numbers and returns the result.
    
    Parameters:
        num1: The first number.
        num2: The second number.
    
    Returns:
        The sum of num1 and num2.
    """
    return num1 + num2

print(add_values(1, 2))             # Output: 3

# ----------- O(log n) order complexity
# Binary search has a time complexity of O(log n)

# ----------- O(n) order complexity
# Linear search has a time complexity of O(n)

# ----------- O(n log n) order complexity
# Merge Sort has a time complexity of O(n log n)

# ----------- O(n ^ 2) order complexity
# Bubble sort has a time complexity of O(n^2) in the worst and 
# average cases
# Insertion Sort also has a time complexity of O(n^2)

# ----------- O(2 ^ n) order complexity

def fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursion. The Fibonacci sequence is 
    a series of numbers where each number is the sum of the two preceding ones.
    
    Parameters:
        n (int): The index of the Fibonacci number to calculate.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n  # Base case: return n if n is 0 or 1
    else:
        # Recursive case: calculate the sum of the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = 5
print(fibonacci(n))  # Output: 5 (fibonacci(5) = 5)

"""
The time complexity of this recursive approach is O(2^n) because 
for each call to the fibonacci function, 
it makes two recursive calls: one for fibonacci(n - 1) and 
another for fibonacci(n - 2).
"""
