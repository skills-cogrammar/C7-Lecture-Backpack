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
from a module using the from ... import ... syntax.
"""
# my_main.py
from my_module import greet

message = greet("Bob")
print(message)  # Output: Hello, Bob!

""" ----- Importing with Aliases:
You can import a module or specific items from a module with an alias 
using the as keyword.
"""
# my_main.py
import my_module as mm

message = mm.greet("Charlie")
print(message)  # Output: Hello, Charlie!
