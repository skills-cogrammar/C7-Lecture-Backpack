#With parameter & return statement
def add(num1,num2): #parameters
    """"This function returns the sum of num1 and num2"""
    return num1 + num2

sum_value = add(10,20)
print(sum_value)

print(add(20,30))
#print(add(2,430))
#print(add(5,130))

#Without parameter
def greet():
    print("Hi, my name is Luke.")

greet()

#With parameter
def greet_1(a):
    print(f"Hi, my name is {a}.")

greet_1("Leia")

#f-string with a built-in function
random_text = input("What is your favourite food?")
print(f"We are out of {random_text} today.")

#print(int(3.2))
#int, str, float

print(f"Length of user input: {len(random_text)} \n Sorry, that you cannot eat {random_text} today.")
    
#Using loops inside functions
def my_func(cars):
    for x in cars:
        print(x)

cars = ["Polo","X-trail","Jazz"] #Polo  

my_func(cars)