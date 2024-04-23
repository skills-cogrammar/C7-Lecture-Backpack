import insertion_sort, bubble_sort

num_items = int(input("Please enter the amount of items in the list that must be sorted: "))
lst = []

for i in range(num_items):
    item = int(input("Enter item to have in list: "))
    lst.append(item)


print(f"Your list is: {lst}")

bubble_sort_lst = bubble_sort.sort(lst)
insertion_sort_lst = insertion_sort.sort(lst)
selecton_sort_lst = insertion_sort.sort(lst)

print(f"Your sorted list is: {bubble_sort_lst}")
print(f"Your sorted list is: {insertion_sort_lst}")
print(f"Your sorted list is: {selecton_sort_lst}")