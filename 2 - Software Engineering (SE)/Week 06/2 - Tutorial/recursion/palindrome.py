"""
Write a short recursive C++ function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, "racecar"
and "gohangasalamiimalasagnahog" are palindromes.
"""

class CheckIfPalindrome():
    def __init__(self):
        pass  # Constructor method, does nothing

    def check_if_palindrome_iterative(self, word):
        # Initialize variables
        last_char = len(word) - 1
        count = 0
        
        # Loop until count is less than the index of the last character
        while count < last_char:
            # Check if characters at count and last_char positions are equal
            if word[count] == word[last_char]:
                count += 1
                last_char -= 1
            else:
                break  # If not equal, break out of the loop
        
        # Calculate the halfway point of the word
        occ = len(word) // 2
        
        # Check if count is equal to the halfway point
        if count == occ: 
            return True  # Return True if the word is a palindrome
        else: 
            return False  # Return False if the word is not a palindrome

    def check_if_palindrome_recursive(self, word, idx_start, idx_end):
        # Check if characters at idx_start and idx_end are equal and if idx_start is less than idx_end
        if (word[idx_start] == word[idx_end]) and (idx_start < idx_end):
            # If true, call the method recursively with updated indices
            self.check_if_palindrome_recursive(word, idx_start + 1, idx_end - 1)
        
        # If characters at idx_start and idx_end are not equal, return False
        if word[idx_start] != word[idx_end]:
            return False
        
        return True  # If all characters checked and found to be equal, return True

word = "gohangasalamiimalasagnahog"

# Check palindrome iteratively
print(CheckIfPalindrome().check_if_palindrome_iterative(word))

# Check palindrome recursively
count = 0
last_char = len(word) - 1
print(CheckIfPalindrome().check_if_palindrome_recursive(word, count, last_char))
