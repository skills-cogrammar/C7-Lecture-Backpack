def binary_search(value, my_list):
    low, high = 0, len(my_list)-1
    while high >= low:
        # Get mid point
        mid = (low + high) // 2

        # If value is found at mid point return
        if my_list[mid] == value:
            return mid
        # If value is larger then the mid point value set low
        # to mid selecting the second half of the list
        elif my_list[mid] < value:
            low = mid + 1
        # If value is smaller then the mid point value set low
        # to mid selecting the second half of the list
        else:
            high = mid - 1

print(binary_search(5, [0,1,2,3,4,5]))