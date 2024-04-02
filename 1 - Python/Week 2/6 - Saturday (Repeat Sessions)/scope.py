#Random function

def hogwarts(h1, h2):
    print(f"Character 1: {h1}. \n Character 2: {h2}")
    print(f"You have an extra character: {third_char}")

third_char = "Hermione" #This is global variable

hogwarts("Harry","Ron")

def my_func():
    #default: inside the function, it is a local variable
    global y #If this is not global, last statement print(y) won't work 
    y = "Here comes the sun"
    print (y)

my_func()
print(y)