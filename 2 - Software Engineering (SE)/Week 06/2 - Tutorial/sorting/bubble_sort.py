# Bubble sort

# Step 1 − Check if the first element in the input array is greater than the next element in the array.

# Step 2 − If it is greater, swap the two elements; otherwise move the pointer forward in the array.

# Step 3 − Repeat Step 2 until we reach the end of the array.

# Step 4 − Check if the elements are sorted; if not, repeat the same process (Step 1 to Step 3) from the last element of the array to the first.

# Step 5 − The final output achieved is the sorted array.


from swap import swap

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
        swaps = 0
        # Iterate through the unsorted portion of the list.
        for j in range(0, len(lst)-i-1):
            # If the current element is greater than the next element, swap them.
            if lst[j] > lst[j+1]:
                swap(lst, j, j + 1)
                swaps = 1
        # If no swaps were made in this pass, the list is already sorted.
        if swaps == 0:
            break
    # Return the sorted list.
    return lst







