# =============== Searching Algorithms

# ------  Linear Search  ------
"""
Linear search is a simple search algorithm that sequentially checks each element 
of the list until it finds the target value or reaches the end of the list.
It starts at the beginning of the list and iterates through each element, 
comparing it with the target value.
If the target value is found, the index of that value is returned. 
If the target value is not found after iterating through the entire list, 
None is returned.
Linear search has a time complexity of O(n), where n is the number of elements in the list.
"""
def linear_search(value, my_list):
    """
    Performs linear search to find the index of a value in a list.
    
    Parameters:
        value: The value to search for.
        my_list (list): The list to search within.
        
    Returns:
        int or None: The index of the value if found, otherwise None.
    """
    # Iterate over items until correct value is found
    # Return value if found, otherwise return None if value is not found
    for i in range(len(my_list)):
        if my_list[i] == value:
            return i
    return None

my_list = [2, 5, 3, 7, 6, 4]
print(linear_search(5, my_list))  # Output: 1
print(my_list[1])  # Output: 5

# ------  Binary Search  ------
"""
Binary search is a more efficient search algorithm that works on SORTED LISTS.
It compares the target value with the middle element of the list. If they are equal, 
the search is successful, and the index of the middle element is returned.
If the target value is less than the middle element, the search continues 
in the lower half of the list. If the target value is greater than the middle element, 
the search continues in the upper half of the list.
The search repeatedly halves the search interval until the target value is found 
or the interval becomes empty.
Binary search has a time complexity of O(log n), where n 
is the number of elements in the list. This makes it significantly faster 
than linear search for large lists.
"""
def binary_search(value, my_list):
    """
    Performs binary search to find the index of a value in a sorted list.
    
    Parameters:
        value: The value to search for.
        my_list (list): The sorted list to search within.
        
    Returns:
        int or None: The index of the value if found, otherwise None.
    """
    low, high = 0, len(my_list) - 1
    while high >= low:
        # Get mid point
        mid = (low + high) // 2

        # If value is found at mid point, return mid
        if my_list[mid] == value:
            return mid
        # If value is larger than the mid point value, set low
        # to mid, selecting the second half of the list
        elif my_list[mid] < value:
            low = mid + 1
        # If value is smaller than the mid point value, set high
        # to mid, selecting the first half of the list
        else:
            high = mid - 1
    return None

print(binary_search(5, [0, 1, 2, 3, 4, 5]))  # Output: 5
