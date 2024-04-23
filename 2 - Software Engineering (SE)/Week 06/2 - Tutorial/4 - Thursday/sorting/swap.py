def swap(lst, value_1, value_2):
    # Swap two values in a list given their indices
    # Using tuple unpacking to swap values without a temporary variable


    # # Alternative
    # tmp = lst[value_1]
    # lst[value_1] = lst[value_2]
    # lst[value_2] = tmp

    lst[value_1], lst[value_2] = lst[value_2], lst[value_1]
    return lst  # Return the modified list

# arr = [1,2,3]

# # [2,1,3]

# print(swap(arr, 0,1))