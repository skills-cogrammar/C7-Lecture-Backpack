# Insertion sort

# Step 1 − Set MIN to location 0.

# Step 2 − Search the minimum element in the list.

# Step 3 − Swap with value at location MIN.

# Step 4 − Increment MIN to point to next element.

# Step 5 − Repeat until the list is sorted.

from swap import swap

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
        swap(lst, i, min_value_idx)
    # Return the sorted list.
    return lst