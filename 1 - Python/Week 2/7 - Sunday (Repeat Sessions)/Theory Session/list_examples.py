# Example 1 - Indexing
# string list
# my_pokemon = ["squirtle", "metapod", "pikachu", "charizard", "gengar"]

# number list
# number_list = [12, 34, 56, -100, 12.4, -1]

# Mixed list
mixed_list = [[12, 34], "apple cider vinegar", 12, True]
#                0               1             2     3
#            mixedList[0] = [12, 34]
#                            0    1
#            mixedlist[0][1] = 34   

# # indexing second value within first list item
print(mixed_list[0][1])

# # getting last bool value
print(type(mixed_list[-1]))

# index a word or character within list
print(mixed_list[1][1])  # will return second character in string

# grabbing string
print(mixed_list[1])

# splitting string up by common character 
print(mixed_list[1].split(" "))

# indexing split up word (list) to access the word 'cider'
print(mixed_list[1].split(" ")[1])

# it does not modify the original list
print(mixed_list)

######################################################################################################################

my_pokemon = ["squirtle", "metapod", "pikachu", "charizard", "gengar"]

# Adding garfield to the end of list
my_pokemon.append("garfield")
# print(my_pokemon)

# creating new list
late_catch = ["venusaur", "slowpoke", "arbok"]

# adding new list to original list
my_pokemon.extend(late_catch)
# print(my_pokemon)

# removing garfield by use of 'remove' function
my_pokemon.remove("garfield")
# print(my_pokemon)

# using pop() to remove garfield [NOTE: will only work if the remove hasn't been called, keep that in mind] 
imposter_poke = my_pokemon.pop(5)
print(f"{imposter_poke} has crossed the multi-verse and should not be here")
print(my_pokemon)

# remvoing last item
my_pokemon.pop()
print(my_pokemon)

#######################################################################################################################

count = 0
for pokemon in my_pokemon:
    print(pokemon)
    count += 1
    print(count)

    if pokemon == "gengar":
        print(f"{pokemon} has been found at position {count}")
        break

print(f"Value stored inside count is: {count}")
print(f"The 5th pokemon {count} in the list 'my_pokemon' is: {my_pokemon[count-1]}")


number_list = [12, 34, 56, -100, 12.4, -1]

# sort()
print("List before sort:")
print(number_list)

print("List after sort:")
number_list.sort()  # sorting in natural order
number_list.sort(reverse=True)  # sorting in reverse
print(number_list)


# sorted 
print("Original List before sort:")
print(number_list)

print("Original List after sort:")
new_sorted_list = sorted(number_list)
print(number_list)

print("New sorted list")
print(new_sorted_list)

# sort() - will alter the original list
# sorted() - will create a sorted copy of the original list


# Sort with words
print("List before sort:")
print(my_pokemon)

print("List after sort:")
# my_pokemon.sort()  # sorting in natural order
my_pokemon.sort(reverse=True)  # sorting in reverse
print(my_pokemon)



# New mixed list
new_mixed_list = [12, "gengar", 56.78, "slowpoke", True, -3, "ekans"]

# new_mixed_list.sort()

# sorted method without unique constraints
# sorted_list = sorted(new_mixed_list)

# will throw exception/error
# print(sorted_list)

# 
print(new_mixed_list)
# The line `sorted_list = sorted(new_mixed_list, key=lambda x: str(x))` is sorting the
# `new_mixed_list` in a customized way.

"""
 The `key=lambda x: str(x)` is a parameter used in the `sorted()` function to 
 specify a custom sorting key. In this case, it is converting each element `x`
 in the list to a string using `str(x)` before sorting. This allows the 
 `sorted()`function to sort the elements based on their string representations
 rather than their original data types.
"""

sorted_list = sorted(new_mixed_list, key=lambda x: str(x))

print(sorted_list) 

print(type(sorted_list[3])) 
