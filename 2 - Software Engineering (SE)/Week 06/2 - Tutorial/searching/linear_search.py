def linear_search(lst, key):
    """
    Perform linear search to find the index of the given key in the list.

    Parameters:
        lst (list): The list to be searched.
        key: The value to be searched for in the list.

    Returns:
        int: The index of the key in the list if found, otherwise -1.
    """
    # Iterate through the list.
    for i in range(len(lst)):
        # If the current element is equal to the key, return its index.
        if lst[i] == key:
            return i
    # If key is not found in the list, return -1.
    return -1
