def bubble_sort(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        for j in range(1, i + 1):
            if my_list[j-1] > my_list[j]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
    return my_list


print(bubble_sort([4,6,7,3,2,5]))

