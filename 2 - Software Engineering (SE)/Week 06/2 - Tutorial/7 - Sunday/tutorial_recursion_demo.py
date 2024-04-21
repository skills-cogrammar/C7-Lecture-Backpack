# ============ Function to calculate the factorial of a number recursively
def factorial(number):
    """
    Calculates the factorial of a number using recursion.
    Factorial => 5 => 5 * 4 * 3 * 2 * 1 => 5! = Output: 120

    Parameters:
        number (int): The number for which factorial is to be calculated.

    Returns:
        int: The factorial of the input number.
    """
    # Recursive Case:
    if number != 0 and number != 1:
        return number * factorial(number - 1)
    # Base Case:
    else: 
        return 1

# Coding portion
number = 5
if number >= 0:
    print(factorial(5))  # Output: 120
else:
    print("--> You have provide a negative number.")


# ============ Compute the product of two positive integers
class Product:
    """
    Provides methods to compute the product of two positive integers
    """
    def product(self, a, b):
        """
        Computes the product of two positive integers using recursion.

        Parameters:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The product of a and b.
        """
        # Base Case:
        if b == 0:
            return 0
        # Recursive Case:
        else:
            return a + self.product(a, b-1)

    def product_normal(self, a, b):
        """
        Computes the product of two positive integers using the '*' operator.

        Parameters:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The product of a and b.
        """
        return a * b

    def product_iterative(self, a, b):
        """
        Computes the product of two positive integers iteratively.

        Parameters:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The product of a and b.
        """
        prod = 0
        for _ in range(0, b):
            prod = a + prod

        return prod

# Example usage of the Product class
print(Product().product(3, 5))  # Output: 15


# ============ Check if a string is a palindrome
class CheckIfPalindrome():
    """
    Provides methods to check if a string is a palindrome.
    racecar
    r - a - c - e - c - a - r
    """
    def check_if_palindrome_iterative(self, word):
        """
        Checks if a string is a palindrome iteratively.

        Parameters:
            word (str): The string to be checked.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        last_char = len(word) - 1
        count = 0
        while count < last_char:
            if word[count] == word[last_char]:
                count += 1
                last_char -=1
            else:
                break
        occ = len(word)//2
        if count == occ:
            return True
        else:
            return False

    def check_if_palindrome_recursive(self, word, idx_start, idx_end):
        """
        Checks if a string is a palindrome recursively.

        Parameters:
            word (str): The string to be checked.
            idx_start (int): The starting index of the string.
            idx_end (int): The ending index of the string.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Recursive Case:
        if (word[idx_start] == word[idx_end]) and (idx_start < idx_end):
            return self.check_if_palindrome_recursive(word, idx_start + 1, idx_end - 1)
        
        # If at any point the characters don't match, the string is not a palindrome, so return False.
        if word[idx_start] != word[idx_end]:
            return False
        
        # Base Case:
        return True 

word = "racingcar"

# Test CheckIfPalindrome Iterative
print(CheckIfPalindrome().check_if_palindrome_iterative(word))  # Output: True

# Test CheckIfPalindrome Recursive
count = 0
last_char = len(word) - 1
print(CheckIfPalindrome().check_if_palindrome_recursive(word, count, last_char))  # Output: True
