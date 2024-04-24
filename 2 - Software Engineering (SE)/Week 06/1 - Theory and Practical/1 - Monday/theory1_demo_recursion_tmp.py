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
pass

# Test the factorial_iterative function
pass

# ---> Recursive version
pass

# Test the factorial function
pass

#     ============ Fibonacci sequence ============
"""
Write a function to generate the nth Fibonacci number.
The Fibonacci sequence is defined as follows:
*   Fibonacci(0) = 0
*   Fibonacci(1) = 1
*   Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) for n > 1.
Example: fibonacci(6) should return 8 (as the 6th Fibonacci number is 8).
"""
# ---> Iteration version
pass

# Test the fibonacci_iterative function
pass

# ---> Recursive version
pass

# Test the fibonacci function
pass

#     ============ sum of digits of a positive integer ============
"""
Write a function to calculate the sum of digits of a positive integer.
Example: sum_of_digits(1234) should return 1 + 2 + 3 + 4 = 10.
"""
# ---> Iteration version
pass

# Test the sum_of_digits_iterative function
pass

# ---> Recursive version
pass

# Test the sum_of_digits function
pass

#     ============ the power of a number ============
"""
Implement a function to calculate the power of a number. 
The power function takes a base number (x) and an exponent (n) 
and returns x raised to the power of n.
"""
# ---> Iteration version
pass

# Test the power_iterative function
pass

# ---> Recursive version
pass

# Test the power function
pass
