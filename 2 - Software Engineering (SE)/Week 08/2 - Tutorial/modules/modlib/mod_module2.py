# Selection sort

def sort(lst):
    """
    Perform selection sort to sort the given list in ascending order.

    Parameters:
        lst (list): The list to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate through the list.
    for i in range(len(lst)):
        # Assume the current index contains the minimum value.
        min_value_idx = i
        # Iterate through the unsorted portion of the list to find the index of the minimum value.
        for j in range(i+1, len(lst)):
            # If a smaller value is found, update the index of the minimum value.
            if lst[j] < lst[min_value_idx]:
                min_value_idx = j
        # Swap the current element with the minimum value found.
        lst[i], lst[min_value_idx] = lst[min_value_idx], lst[i]
    # Return the sorted list.
    return lst
