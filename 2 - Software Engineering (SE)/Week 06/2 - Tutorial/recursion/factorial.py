def factorial(number):
    # This function calculates the factorial of a given non-negative integer recursively.
    # A factorial is the product of an integer and all the integers below it, down to 1.
    # For example, factorial(5) is 5 * 4 * 3 * 2 * 1, which equals 120.
    
    # Base case: if the number is 0, return 1 because 0! is defined as 1.
    if number == 0:
        return 1
    
    # Recursive case: multiply the current number with the factorial of (number - 1).
    # This step continues until the base case is reached (number == 0).
    return number * factorial(number - 1)

# Test the function with the input 5.
# The expected result is 5! = 5 * 4 * 3 * 2 * 1 = 120.
print(factorial(5))
