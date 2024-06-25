#Python program: functions can be 
#treated as objects 
#Passing function to a variable
def greet(text): 
    return text.upper() 
  
print(greet('Hello')) 
intro = greet 
print (intro('Hello World!'))
#Output: HELLO
#HELLO WORLD!


# Pasing functions as arguments to other functions 
def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func, name): 
    # storing the function in a variable 
    greeting = func('Function passed as argument in ' + name) 
    print(greeting)  

greet(shout, "Python") 
greet(whisper, "Python") 
#Output: FUNCTION PASSED AS ARGUMENT IN PYTHON
#function passed as argument in python
                                                                            

#Functions returning another function 
def add_sub(a, b):
    add = a + b
    sub = a - b
    def mult(c):
        print(add * sub * c)
    return mult        
 
# form a object of first method
returned_function = add_sub(5, 2)
#a=5 & b=2 -> add=7 & sub=3
 
# check object
print(returned_function)
#Output: It will be a <function>
 
# call second method by first method
returned_function(10)
#Output: 210 (With c = 10, a*b*c = 210)


#Local Scope
def myfunc():
  x = "Hello!"
  print(x)

#myfunc()
#Output: Hello!

#Nested function
def myfunc():
  x = "Hello"
  def myinnerfunc():
    print(x+" World!")
  myinnerfunc()

myfunc()
#Output: Hello World!

#Scope rules
def scope_test():
    def do_local():
        text = "local text"

    def do_nonlocal():
        nonlocal text
        text = "nonlocal text"

    def do_global():
        global text
        text = "global text"

    text = "sample text"
    do_local()
    print("After local assignment:", text)
    do_nonlocal()
    print("After nonlocal assignment:", text)
    do_global()
    print("After global assignment:", text)

scope_test()
print("In global scope:", text)
#Output: After local assignment: sample text
#After nonlocal assignment: nonlocal text
#After global assignment: nonlocal text
#In global scope: global text

#Closure
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 2
times2 = make_multiplier_of(2)

# Multiplier of 5
times5 = make_multiplier_of(5)

#times2 and times5 are closure functions

print(times2(7))
#Output: 14

print(times5(9))
#Output: 45

print(times5(times2(3)))
# Output: 30

#Pass by reference and value
def call_by_value(x): 
    x = x * 2
    print("In function value updated to", x) 
    return
  
def call_by_reference(list): 
    list.append("D") 
    print("In function list updated to", list) 
    return
  
my_list = ["E"] 
num = 6
print("number before=", num) 
call_by_value(num) 
print("after function num value=", num) 
print("list before",my_list) 
call_by_reference(my_list) 
print("after function list is ",my_list)

#Pass by value
a = 10
b = a
  
a = 20
  
print(a) #Outputs: 20
print(b) #Outputs: 10 


# Pass by reference
obj1 = {'value': 10}
obj2 = obj1

obj1['value'] = 20

print(obj1['value'])  #Outputs: 20
print(obj2['value'])  #Outputs: 20


x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is now', x)


x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func()
print('Value of x is', x)

