# def validate_input(value):
#     if not isinstance(value,int): 
#         raise ValueError("Hey there coder, the input must be an integer")
    
# try:
#     validate_input("Hello world!")
# except ValueError as e:
#     print(f"Error: {e}")    


#Example 2:
def add_num(n1,n2):
    if not (isinstance(n1, (int, float)) and isinstance(n2, (int,float))):
        raise ValueError("Both the numbers n1 and n2 should be either an integer or a float.")
    return n1 + n2


#Enclose calling the function in a try except block
# try:
#     print('The sum is: ',add_num(20,"56"))
# except ValueError as ele:
#     print(f"Error: {ele}")  

# print("This is the end, beautiful friend.")

## try (if else) except
try:
    var1 = int(input("Enter the number of muffins stolen: "))
    print(f"Gosh! {var1} muffins! That is a lot for sure!")
except ValueError:
    print("Muffins are whole items! Please enter an integer value, e.g. 42")
except NameError as e:
    print(f"Error: {e}")

while True:
    try:
        order1 = int(input("How many muffins do you want?"))    
        if order1 >= 1:
            print(f"You have ordered {order1} muffins. Enjoy your day!")
        else:
            print("You have not ordered any muffins. Good bye!")
        break
    except ValueError:
        print("You cannot have fractional muffins. Please enter an integer value.")







