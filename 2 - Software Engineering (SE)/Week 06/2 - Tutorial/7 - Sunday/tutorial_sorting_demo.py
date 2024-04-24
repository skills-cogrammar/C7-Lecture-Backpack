# =============  Bubble sort

# Import bubble sort function to simplify code
# --> From folder my_library import file bub_sort
from my_library import bub_sort

# ------ Test the sort
lst = [5,3,2,9,6,1]
bubble_sort_lst = bub_sort.sort(lst)

print(f"Your sorted list is: {bubble_sort_lst}")

# =============  Insertion sort

# Import insertion sort function to simplify code
from my_library import ins_sort

# ------ Test the sort
lst = [5,3,2,9,6,1]
insertion_sort_lst = ins_sort.sort(lst)

print(f"Your sorted list is: {insertion_sort_lst}")

# ============= Selection sort

# Import insertion sort function to simplify code

from my_library import sel_sort

# ------ Test the sort
lst = [5,3,2,9,6,1]
selection_sort_lst = sel_sort.sort(lst)  

print(f"Your sorted list is: {selection_sort_lst}")
