def binary_search(lst, key):
    """
    Perform binary search to find the index of the given key in the sorted list.

    Parameters:
        lst (list): The sorted list to be searched.
        key: The value to be searched for in the list.

    Returns:
        int: The index of the key in the list if found, otherwise -1.
    """
    # Initialize left pointer to the beginning of the list.
    left = 0
    # Initialize right pointer to the end of the list.
    right = len(lst) - 1

    # Loop until left pointer is less than or equal to the right pointer.
    while left <= right:
        # Calculate the middle index.
        mid = (left + right) // 2

        # If the middle element is equal to the key, return its index.
        if lst[mid] == key:
            return mid
        
        # If the middle element is less than the key, update left pointer to search in the right half.
        if lst[mid] < key:
            left = mid + 1
        # If the middle element is greater than the key, update right pointer to search in the left half.
        else:
            right = mid - 1

    # If the key is not found in the list, return -1.
    return -1

def binary_search_recursive(lst, min_pt, max_pt, key):
# def binary_search_recursive(lst, key):
    # mid = len(lst) // 2
    mid = (min_pt + max_pt) // 2
    if lst[mid] == key:
        return mid
    if lst[mid] > key:
        # lst = lst[:mid]
        # return binary_search_recursive(lst, key)

        return binary_search_recursive(lst, min_pt, mid - 1, key)
    else:
        # lst = lst[mid:]
        # return binary_search_recursive(lst, key)

        return binary_search_recursive(lst,mid + 1, max_pt, key)