"""     ============ general structure of a recursive function ============
Here's a general structure of a recursive function incorporating both 
base cases and recursive cases:

*   The function first checks for base cases using if statements.
*   If the base condition is met, the function returns the base result directly.
*   If the base condition is not met, the function proceeds to the recursive case(s).
*   It modifies the input parameters and makes a recursive call to itself 
    with the modified input.
*   The process continues recursively until the base case(s) are reached, 
    at which point the recursion unwinds and returns the final result 
    back up the call stack.

def recursive_function(input):
    # Base case(s)
    if base_condition(input):
        # Return the result directly
        return base_result

    # Recursive case(s)
    else:
        # Modify the input and make a recursive call
        modified_input = modify_input(input)
        recursive_result = recursive_function(modified_input)
        
        # Further processing of the recursive result
        final_result = process_result(recursive_result)
        return final_result
"""

#     ============ factorial of a non-negative integer ============
"""
Write a function to calculate the factorial of a non-negative integer.
The factorial of n (denoted as n!) is the product of all positive integers less 
than or equal to n.
Example: factorial(5) should return 5 * 4 * 3 * 2 * 1 = 120.
"""
# ---> Iteration version
def factorial_iterative(factorial_number):
    result = 1
    # Iterate from 1 to n and multiply each number with the result
    
    for number in range(1, factorial_number + 1): # Ex. [1,2,3,4,5]
        result *= number        # result = result * number
    return result

# Test the factorial_iterative function
print(factorial_iterative(5))  # Output: 120
# Example: factorial(5) should return 5 * 4 * 3 * 2 * 1 = 120.

# ---> Recursive version
def factorial(n):
    # Base Case: If n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive Case: Calculate factorial recursively
    else:
        return n * factorial(n - 1)

"""
5 => return 5 * factorial(4)    
4 => return 4 * factorial(3)
3 => return 3 * factorial(2)
2 => return 2 * factorial(1)
1 => return 1

1 => return 1
2 => return 2 * 1
3 => return 3 * 2
4 => return 4 * 6
5 => return 5 * 24
Answer 120

"""

# Test the factorial function
print(factorial(5))  # Output: 120

#     ============ Fibonacci sequence ============
"""
Write a function to generate the nth Fibonacci number.
The Fibonacci sequence is defined as follows:
*   Fibonacci(0) = 0
*   Fibonacci(1) = 1
*   Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) for n > 1.

Fibonacci numbers are a sequence of numbers in which each number is 
the sum of the two preceding ones, usually starting with 0 and 1. 
The sequence starts as follows:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...        # Note that the number 1 occurs twice

Example: fibonacci(6) should return 8 (as the 6th Fibonacci number is 8).
"""
# ---> Iteration version
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next

    return fib_curr

# Test the fibonacci_iterative function
print(fibonacci_iterative(6))       #Output: 8

# ---> Recursive version
def fibonacci(n):
    # Base Case: fibonacci(0) = 0, fibonacci(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Case: Calculate Fibonacci Recursively
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Test the fibonacci function
result = fibonacci(6)
print(result)
print(fibonacci(6))

#     ============ sum of digits of a positive integer ============
"""
Write a function to calculate the sum of digits of a positive integer.
Example: sum_of_digits(1234) should return 1 + 2 + 3 + 4 = 10.
"""
# ---> Iteration version
def sum_of_digits_iterative(n):
    # Initialize the sum variable to store the sum of digits
    sum_digits = 0
    
    # Iterate through each digit of the number
    while n > 0:
        # Extract the last digit of the number and add it to the sum
        digit = n % 10
        sum_digits += digit
        # Remove the last digit from the number
        n //= 10
    
    return sum_digits

# Test the sum_of_digits_iterative function
print(sum_of_digits_iterative(1234))  # Output: 10 (1 + 2 + 3 + 4 = 10)

# ---> Recursive version
def sum_of_digits(n):
    # Base case: If the number is a single digit, return the number itself
    if n < 10:
        return n
    # Recursive case: Calculate sum of digits recursively
    else:
        # Extract the last digit and add it to the sum of digits of the remaining number
        return n % 10 + sum_of_digits(n // 10)

# Test the sum_of_digits function
print(sum_of_digits(1234))  # Output: 10 (1 + 2 + 3 + 4 = 10)

#     ============ the power of a number ============
"""
Implement a function to calculate the power of a number. 
The power function takes a base number (x) and an exponent (n) 
and returns x raised to the power of n.
"""
# ---> Iteration version
def power_iterative(x, n):
    result = 1
    # Iterate n times and multiply result by x in each iteration
    for _ in range(n):
        result *= x
    return result

# Test the power_iterative function
print(power_iterative(2, 3))  # Output: 8 (2^3 = 2 * 2 * 2 = 8)

# ---> Recursive version
def power(x, n):
    # Base case: If the exponent is 0, return 1
    if n == 0:
        return 1
    # Recursive case: Calculate power recursively
    else:
        return x * power(x, n - 1)

# Test the power function
print(power(2, 3))  # Output: 8 (2^3 = 2 * 2 * 2 = 8)
