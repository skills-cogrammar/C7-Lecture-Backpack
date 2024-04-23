from linear_search import linear_search
from binary_search import binary_search


lst = [1,2,3,4,5,6,7,8,9]

key_to_search = 9

# In python, lst.index(key_to_search)

# Perform linear search on the list to find the index of key 9 and print the result.
print(linear_search(lst, key_to_search))

# Perform binary search on the list to find the index of key 9 and print the result.
print(binary_search(lst, key_to_search))