# Bubble sort

def sort(lst):
    """
    Perform bubble sort to sort the given list in ascending order.

    Parameters:
        lst (list): The list to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate through the list.
    for i in range(len(lst)):
        num_swaps = 0
        # Iterate through the unsorted portion of the list.
        for j in range(0, len(lst)-i-1):
            # If the current element is greater than the next element, swap them.
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                num_swaps = 1
        # If no swaps were made in this pass, the list is already sorted.
        if num_swaps == 0:
            break
    # Return the sorted list.
    return lst
