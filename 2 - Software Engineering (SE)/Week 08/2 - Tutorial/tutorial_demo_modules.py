"""   ============= my_main.py
Creating and importing modules in Python is a fundamental aspect of 
code organisation and reuse. 

Here's how you can create and import modules:
"""

""" ----- Creating a Module:
To create a module, simply write your Python code in a .py file. 
This file will serve as your module.

For example, let's say you want to create a module named my_module.py. 
You can create this file in your project directory and 
write your Python code inside it.
"""
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def depart(name):
    return f"Later, {name}!"

""" ----- Using the Module:
Once you've created your module, you can use its functions, classes, and variables 
in other Python scripts or modules.

To use all the functions from the my_module module, 
you need to import the module into your Python script.
"""
# my_main.py
import my_module

message = my_module.greet("Alice")
print(message)  # Output: Hello, Alice!

""" ----- Importing Specific Items:
You can also import specific items (functions, classes, variables) 
from a module in the root directory using the from ... import ... syntax.
"""
# my_main.py
from my_module import greet

message = greet("Bob")
print(message)  # Output: Hello, Bob!

"""
If the modules are in a separate folder called eg. \modulelib then use the below.
"""
from modulelib.my_module2 import greet

"""
If the modules are in a multi folder structure eg. \modulelib\interestcalc\my_module3.py
"""
from modulelib.interestcalc.my_module3 import greet

""" ----- Importing with Aliases:
You can import a module or specific items from a module with an alias 
using the as keyword.
"""
# my_main.py
import my_module as mm

message = mm.greet("Charlie")
print(message)  # Output: Hello, Charlie!

""" ----- Running Modules as Scripts:
You can also run a Python module as a script by using the module's file name. 
This allows you to execute code within the module directly from the command line.
"""
# > python my_module.py

""" =========== math_main.py
Here's an example of creating a custom module named math_operations.py 
and importing it into a Python script:
"""
#### Custom Module: math_operations.py
# Place the below code into the file math_operations.py

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

#### Python Script: math_main.py

# Importing the custom module math_operations
from math_operations import add, subtract, multiply, divide

# Using functions from the custom module
result_add = add(5, 3)
print("Addition Result:", result_add)

result_subtract = subtract(10, 4)
print("Subtraction Result:", result_subtract)

result_multiply = multiply(7, 2)
print("Multiplication Result:", result_multiply)

result_divide = divide(20, 5)
print("Division Result:", result_divide)

"""
When you run math_main.py, it will import the specific functions from the
math_operations module to perform arithmetic operations. This will support
namespacing since if someone add a function in the future that is not part
of the current code, then the new function will not be included in the import.
"""
"""
----- Resolving Naming Conflicts
Suppose we have three modules, each containing a sort function:
Create a folder called /resolve and create modules and main in this folder
"""
# Module mod_module1.py:
def sort(data):
    # Sorting implementation specific to module1
    return sorted_data

# Module mod_module2.py:
def sort(data):
    # Sorting implementation specific to module2
    return sorted_data

# Module mod_module3.py:
def sort(data):
    # Sorting implementation specific to module3
    return sorted_data

"""Now, let's import these modules into another script mod_main.py and 
resolve the naming conflicts using aliasing:
"""

# Importing modules with aliasing
import modlib.mod_module1 as m1
import modlib.mod_module2 as m2
import modlib.mod_module3 as m3

# Using the sort functions from each module
data1 = [3, 1, 2]
sorted_data1 = m1.sort(data1)

data2 = [7, 5, 6]
sorted_data2 = m2.sort(data2)

data3 = [9, 8, 10]
sorted_data3 = m3.sort(data3)

# Printing the sorted data
print("Sorted data from module1:", sorted_data1)
print("Sorted data from module2:", sorted_data2)
print("Sorted data from module3:", sorted_data3)

""" =========== Explore the use of third-party modules and packages from the 
Python Package Index (PyPI).

--- Browsing PyPI: 
Visit the PyPI website (https://pypi.org/) to browse and search for packages. 
"""
