# O(1)
def get_value(my_list, key):
    return my_list[key]

print(get_value([1,2,3,4,5], 1))


def add_values(num1, num2):
    return num1 + num2

























def get_values(my_list, keys):
    values = []
    for key in keys:
        values.append(my_list[key])
    return values

# O(n)






















def print_list(lst):
    # O(nLog(n))
    lst.sort()

    # O(n)
    for item in lst:
        print(item)

# nLog(n)

















def double_print(lst):
    for _ in range(len(lst)): # n
        for item in lst: # n
            print(item)
    
    # O(n^2) = n * n

double_print([1,2,3,4,5])
