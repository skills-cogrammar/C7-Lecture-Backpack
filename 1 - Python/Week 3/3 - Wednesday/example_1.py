# Example 1
def validate_input(value):
    if not isinstance(value, int): 
        raise ValueError("Input must be an integer")
    
    
# # validate_input("hi")

try:
    validate_input("hello")
except ValueError as e:
    print(f"Error: {e}")


# Example 2
# True - 1
# False - 0
    
# print(True + True)

# enter either float or integer
def add_num(num1, num2):

    #               True                   and         True
    #              (       entire statement is true         )   
    #  true        (              false               ) 
    # if not true then do this 👇
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise ValueError("Both values should either be int or float")
    return num1 + num2


print(add_num(26, 10))   # this should work

# Enclose this within try to gracefully return the error
try:
    print(add_num(23, "10"))  
except ValueError as e:
    print(f"Error: {e}")