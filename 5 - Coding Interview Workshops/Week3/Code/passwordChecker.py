# Example program

import math

def calculate_classical_permutation(n, r):
    """
    Calculate permutations of r out of n items using the classical permutation formula.
    This scenario assumes no repetition of items.
    """
    return math.factorial(n) // math.factorial(n - r)

def calculate_classical_combination(n, r):
    """
    Calculate combinations of r out of n items using the classical combination formula.
    Order does not matter in this scenario.
    """
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def calculate_probability(total_outcomes, successful_outcomes):
    """
    Calculate the probability of a specific outcome given the total number of outcomes.
    """
    return successful_outcomes / total_outcomes

def is_valid_group(char_set, specific_group):
    """
    Check if the specific group of characters exists within the initial character set.
    """
    return all(specific_group.count(char) <= char_set.count(char) for char in specific_group)

# User input for the character set
char_set = input("Enter the set of characters (e.g., 'abcdef'): ")
n = len(char_set)

# User input for permutation
r_permutation = int(input(f"Enter the number of characters to arrange from the set of {n} characters (permutation): "))
unique_arrangements = calculate_classical_permutation(n, r_permutation)
print(f"Number of unique arrangements (permutations) of {r_permutation} out of {n} characters: {unique_arrangements}")

# Calculate and print the probability for a specific arrangement
if r_permutation <= n:
    specific_arrangement = input(f"Enter the specific arrangement of {r_permutation} characters to calculate its probability: ")
    while len(specific_arrangement) != r_permutation or not is_valid_group(char_set, specific_arrangement):
        print(f"The specific arrangement must be {r_permutation} characters long and use only characters from the initial set '{char_set}'.")
        specific_arrangement = input(f"Re-enter the specific arrangement: ")
    probability_of_arrangement = calculate_probability(unique_arrangements, 1)
    print(f"Probability of randomly arranging the sequence '{specific_arrangement}': {probability_of_arrangement:.4f}")
else:
    print(f"Cannot have more characters in the arrangement than are available in the set.")


# User input for combination
r_combination = int(input(f"Enter the number of characters to choose from the set of {n} characters (combination): "))
unique_groups = calculate_classical_combination(n, r_combination)
print(f"Number of unique groups (combinations) of {r_combination} out of {n} characters: {unique_groups}")

if r_combination <= n:
    specific_combination = input(f"Enter the specific group of {r_combination} characters to calculate its probability: ")
    while not is_valid_group(char_set, specific_combination) or len(specific_combination) != r_combination:
        print(f"The specific group must be {r_combination} characters long and use only characters from the initial set '{char_set}'.")
        specific_combination = input(f"Re-enter the specific group: ")
    probability_of_combination = calculate_probability(unique_groups, 1)
    print(f"Probability of randomly choosing the group '{specific_combination}': {probability_of_combination:.4f}")
else:
    print(f"Cannot have more characters in the group than are available in the set.")
