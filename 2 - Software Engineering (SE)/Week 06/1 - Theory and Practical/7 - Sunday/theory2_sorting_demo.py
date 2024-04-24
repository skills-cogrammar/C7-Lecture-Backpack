# =============== Sorting Algorithms

# ------  Bubble Sort  ------
"""
Bubble sort works by repeatedly stepping through the list, 
comparing adjacent elements, and swapping them if 
they are in the wrong order.
It passes through the list multiple times, with each pass 
placing the largest unsorted element at its correct position.
The algorithm terminates when no swaps are needed in a pass, 
indicating that the list is sorted.
Bubble sort has a time complexity of O(n^2) in the worst and 
average cases, making it inefficient for large lists.
"""
def bubble_sort(my_list):
    """
    Sorts a list in ascending order using 
    the bubble sort algorithm.
    
    Parameters:
        my_list (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    for i in range(len(my_list) - 1, -1, -1):
        for j in range(1, i + 1):
            if my_list[j-1] > my_list[j]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
    return my_list

print(bubble_sort([4,6,7,3,2,5]))

# ------  Insertion Sort  ------
"""
Insertion sort works by building a sorted list one element at a time.
It iterates through the list, considering one element at a time and 
inserting it into its correct position in the sorted part of the list.
It maintains a sublist to the left of the current element, which is always sorted.
For each element, it compares it with elements in the sorted sublist and 
shifts larger elements to the right to make space for the current element.
Insertion sort has a time complexity of O(n^2) in the worst and 
average cases but performs well on small lists or nearly sorted lists.
"""
def insertion_sort(my_list):
    """
    Sorts a list in ascending order using 
    the insertion sort algorithm.
    
    Parameters:
        my_list (list): The list to be sorted in-place.
    """
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key

my_list = [12, 11, 13, 5, 6, 1, -1]
insertion_sort(my_list)
print("Sorted list is:", my_list)

# ------  Selection Sort  ------
"""
Selection sort works by repeatedly selecting the smallest element from 
the unsorted part of the list and swapping it with the element at 
the beginning of the unsorted part.
It divides the list into two sublists: sorted and unsorted.
It finds the smallest element in the unsorted sublist and swaps it with 
the first element of the unsorted sublist.
It then moves the boundary of the sorted sublist one element to the right.
Selection sort has a time complexity of O(n^2) in all cases but performs 
fewer swaps compared to bubble sort.
"""
def selection_sort(my_list):
    """
    Sorts a list in ascending order using 
    the selection sort algorithm.
    
    Parameters:
        my_list (list): The list to be sorted in-place.
    """
    n = len(my_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

my_list = [64, 25, 12, 22, 11, 1, -1]
selection_sort(my_list)
print("Sorted list is:", my_list)

# ------  Merge Sort  ------
"""
Merge sort is a divide-and-conquer sorting algorithm that works by 
recursively dividing the input list into smaller sublists, sorting them independently, 
and then merging the sorted sublists to produce a final sorted list. 

Divide -> The first step is to divide the list into two halves recursively until each 
sublist contains only one element. This process continues until the sublists cannot be divided further.

Conquer -> After dividing the list, the algorithm starts merging the divided sublists in a sorted order. 
It compares elements from the two sorted sublists and merges them into a single sorted sublist.

Merge -> During the merge step, the algorithm compares the elements of the two sublists and 
selects the smallest element among them. It then places the selected element into the merged list. 
This process continues until all elements from both sublists are merged into the final sorted list.

Repeat -> Steps 1 to 3 are repeated recursively for each divided sublist until the entire list is sorted.
"""
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2  # Find the middle index
        
        # Divide the list into two halves
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        
        # Recursive call to sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        merge(my_list, left_half, right_half)

def merge(my_list, left_half, right_half):
    i = j = k = 0  # Initialize pointers for left_half, right_half, and merged list
    
    # Compare elements from left_half and right_half and merge into my_list
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            my_list[k] = left_half[i]
            i += 1
        else:
            my_list[k] = right_half[j]
            j += 1
        k += 1
    
    # Copy remaining elements from left_half (if any)
    while i < len(left_half):
        my_list[k] = left_half[i]
        i += 1
        k += 1
    
    # Copy remaining elements from right_half (if any)
    while j < len(right_half):
        my_list[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
my_list = [12, 11, 13, 5, 6, 7]
print("Original list:", my_list)
merge_sort(my_list)
print("Sorted list:", my_list)
