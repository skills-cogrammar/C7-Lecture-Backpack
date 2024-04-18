"""
Write a short recursive C++ function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, "racecar"
and "gohangasalamiimalasagnahog" are palindromes.
"""

class CheckIfPalindrome():
    def __init__(self):
        pass

    def check_if_palindrome_iterative(self, word):
        pass


    def check_if_palindrome_recursive(self, word, idx_start, idx_end):
        pass

word = "gohangasalamiimalasagnahog"
print(CheckIfPalindrome().check_if_palindrome_iterative(word))

count = 0
last_char = len(word) - 1
print(CheckIfPalindrome().check_if_palindrome_recursive(word, count, last_char))