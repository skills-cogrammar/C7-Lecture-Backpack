def swap(lst, value_1, value_2):
    # tmp = lst[value_1]
    # lst[value_1] = lst[value_2]
    # lst[value_2] = tmp
    lst[value_1], lst[value_2] = lst[value_2], lst[value_1]
    return lst

# arr = [1,2,3]

# # [2,1,3]

# print(swap(arr, 0,1))