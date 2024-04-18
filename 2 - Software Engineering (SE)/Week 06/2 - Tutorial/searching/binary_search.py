def binary_search(lst, key):
    """
    Perform binary search to find the index of the given key in the sorted list.

    Parameters:
        lst (list): The sorted list to be searched.
        key: The value to be searched for in the list.

    Returns:
        int: The index of the key in the list if found, otherwise -1.
    """
    pass

def binary_search_recursive(lst, min_pt, max_pt, key):
    pass

        
# test
lst = [1,2,3,4,5,6,7,8,9]
min_idx = 0
max_idx = len(lst) - 1
print(binary_search_recursive(lst, min_idx, max_idx, 9))