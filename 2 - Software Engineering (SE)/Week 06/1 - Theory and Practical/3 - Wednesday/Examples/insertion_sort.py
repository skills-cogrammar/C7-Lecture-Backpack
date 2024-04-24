def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_list = [12, 11, 13, 5, 6, 1, -1]
insertion_sort(my_list)
print("Sorted array is:", my_list)