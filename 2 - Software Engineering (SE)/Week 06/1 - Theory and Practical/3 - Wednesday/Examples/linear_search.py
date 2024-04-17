def linear_search(value, my_list):
    # Iterate over otems until correct value is found
    # Return value otherwise return none if value is not found
    for i in range(len(my_list)):
        if my_list[i] == value:
            return i
        
my_list = [2,5,3,7,6,4]
print(linear_search(5, my_list))
print(my_list[1])