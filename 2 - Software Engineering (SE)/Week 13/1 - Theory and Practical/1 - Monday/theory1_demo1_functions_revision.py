"""Built-in Pyhton functions ********************* """

print("Hello World!")
name = input("Please enter your name: ")
#----------------------------------
sorted_list = sorted([5,4,7,3,7,9,4,5,6,6,3,8,0,2,5,4,36,7,0])
print(sorted_list)
#----------------------------------
print(isinstance("This is a string!", str)) 
#----------------------------------
rounded_number = round(23.4553254, 2)
print(rounded_number)
#----------------------------------
num = pow(10, 5)
print(num)


"""Importing functions ********************* """

from math import sqrt, gcd

print(sqrt(25))
print(gcd(5, 8, 8, 9, 17))
#----------------------------------
from tabulate import tabulate

table = [["Peter", "Parker", 23],
         ["Carl", "Johnson", 33],
         ["Mike", "Nickleson", 28]]
my_headers = ["Name", "Surname", "Age"]
print(tabulate(table, headers=my_headers))


"""User-defined functions ********************* """

def print_line():
    print("-"*80)

print_line()
print("We can now print lines!")
print_line()
#-----
def print_menu(title, options):
    print_line()
    print((" "*(40-(len(title)//2))), title)
    print_line()
    for i, option in enumerate(options,  1):
        print(i, option, sep=" - ")

print_menu("Calculator", ["Add", "Subtract", "Multiply", "Divide"])
#----------------------------------

#Extend print_line and print_menu functionality above using default values
def print_line(symbol="-", length=80):
    print(symbol*length)


def print_menu(title, options, length):
    print_line(length=length)
    print((" "*((length//2)-(len(title)//2))), title)
    print_line(length=length)
    for i, option in enumerate(options,  1):
        print(i, option, sep=" - ")

print_menu("Calculator", ["Add", "Subtract", "Multiply", "Divide"], 20)

"""Returning values ********************* """

def add(num1, num2):
    return num1 + num2

result = add(5, 6)
result -= 3
print(result)
#----------------------------------
def fahrenheit_to_celsius(value):
    return (value-32) * 5/9

def celsius_to_kelvin(value):
    return value + 273.15

f_value = 60
c_value = fahrenheit_to_celsius(f_value)
k_value = celsius_to_kelvin(c_value)

print(f"{f_value}\xb0F is equal to {round(c_value,3)}\xb0C and {round(k_value,3)}K")
#----------------------------------
def cut_list(lst, section):
    # Calculate the midpoint index of the list
    mid = len(lst) // 2

    # If the section is "top", return the first half of the list
    if section == "top":
        return lst[:mid]
    # If the section is "bot", return the second half of the list
    elif section == "bot":
        return lst[mid:]

# Example usage: cut the list into the "top" section (first half)
print(cut_list([1, 2, 3, 4, 5, 6, 7, 5, 3, 5, 6, 45, 345], "top"))  
# Output: [1, 2, 3, 4, 5, 6]


"""Function Decorators *********************"""

# Define a decorator named `positives_only`
def positives_only(func):
    # Define a wrapper function that will modify the behavior of the original function
    def wrapper(values):
        # Filter out negative numbers from the input list `values`
        values = [i for i in values if i >= 0]
        # Call the original function `func` with the filtered list and return the result
        return func(values)
    # Return the wrapper function
    return wrapper

# Apply the `positives_only` decorator to the `average` function
@positives_only
def average(numbers):
    # Calculate and return the average of the numbers in the list
    return sum(numbers) / len(numbers)

# Test the `average` function with a list that includes negative numbers
print(average([-1, -5, -2, -6, 1, 5, 3, 2])) # Result: [1, 5, 3, 2] / 4 = 2.75


"""Recursion *********************"""
def add_numbers(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + add_numbers(numbers[1:])
    
print(add_numbers([1,2,3]))


"""Higher-order functions *********************"""

words = ["cat", "dog", "monkey", "lion", "tiger"]
print(sorted(words, key=len))   # len() function is passed as key
#----------------------------------
def filter_data(data, func):
    # Apply the given function `func` to each item in the `data` list and include
    # the item in the result list if `func(value)` returns True.
    return [i for i in data if func(i)]

def is_even(value):
    # Check if a given integer `value` is even. Return True if it is, otherwise False.
    return True if value % 2 == 0 else False

def is_digit(value):
    # Check if a given string `value` consists only of digits. Return True if it does, 
    # otherwise False.
    return True if value.isdigit() else False

# Filter the list of integers, keeping only even numbers
print(filter_data([1, 2, 3, 4, 5, 6, 7, 8, 9], is_even))  # Output: [2, 4, 6, 8]

# Filter the list of strings, keeping only those that are digits
print(filter_data(["1", "2", "s", "3", "4", "f", "gg", "s", "r", "5"], is_digit))  
# Output: ["1", "2", "3", "4", "5"]

"""Docstrings *********************"""

from math import pi

def calculate_area(radius : float) -> float:
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :type radius: float
    :return: The area of the circle.
    :rtype: float
    """
    return pi * (radius**2)

print(calculate_area(4))
