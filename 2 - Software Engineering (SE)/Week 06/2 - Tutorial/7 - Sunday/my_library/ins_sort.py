# =============  Insertion sort

# Step 1 − If it is the first element, it is already sorted. return 1;
# Step 2 − Pick next element
# Step 3 − Compare with all elements in the sorted sub-list
# Step 4 − Shift all the elements in the sorted sub-list that is greater than the value to be sorted
# Step 5 − Insert the value
# Step 6 − Repeat until list is sorted

from swap import swap

def sort(lst):
    # Loop through the array starting from the second element
    for i in range(1, len(lst)):

        # Store the current element in a variable 'key'
        key = lst[i]

        # Initialize a variable 'j' to point to the element before the current one
        j = i - 1

        # Move elements of 'lst[0..i-1]', that are greater than 'key', to one position ahead of their current position
        while j >= 0 and lst[j] >= key:

            lst[j + 1] = lst[j]
            j = j - 1

        # Place 'key' into its correct position in the sorted subarray
        lst[j + 1] = key

    return lst
