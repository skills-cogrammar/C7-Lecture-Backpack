# Insertion sort

def sort(lst):
    # Loop through the array starting from the second element
    for i in range(1, len(lst)):

        # Store the current element in a variable 'key'
        key = lst[i]

        # Initialise a variable 'j' to point to the element before the current one
        j = i - 1

        # Move elements of 'lst[0..i-1]', that are greater than 'key', to one position ahead of their current position
        while j >= 0 and lst[j] >= key:

            lst[j + 1] = lst[j]
            j = j - 1

        # Place 'key' into its correct position in the sorted subarray
        lst[j + 1] = key

    return lst
