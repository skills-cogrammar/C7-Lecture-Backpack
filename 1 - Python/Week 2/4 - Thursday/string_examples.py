# Example 1

first_name = "Darth"
secondy_name = "Vader"

# full_name = first_name + " " + secondy_name
full_name = f"{first_name} {secondy_name}"

print(full_name.lower())
print(len(full_name))

# Example 2

# a_long_word = "This is a really long sentence that runs for as long as the 
# page length, and cats are cool, Ps so are dogs."

# new_sent_split = a_long_word.split(",")
# # print(a_long_word)

# # print(new_sent_split[0])
# print(new_sent_split)

# Example 3

list_words = ["cats", "dogs", "oranges", "treehouse", "garfield"]

new_word = " ".join(list_words)
print(new_word)

# Example 4
list_numbers = list(range(0, 5))

print(list_numbers)