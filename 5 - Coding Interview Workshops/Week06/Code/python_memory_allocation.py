# --------- Introduction to Python Memory Management ---------

# Immutable data allocated on the stack
x = 10
y = "Python"

# Objects allocated in the heap
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2}

# --------- Visualizing Local Variables vs Objects ---------

def function():
    # Local variable, stored in the stack
    local_var = 20
    # List (object), stored in the heap
    local_list = [1, 2, 3]
function()
# local_var is no longer accessible here, local_list persists in memory

# --------- Efficiency of Memory Allocation ---------

def compute():
    # Stack allocation is fast
    a = 10
    b = 20
    # Heap allocation, slower but necessary for large data
    data = [i for i in range(10000)] # Just use 20 for Python Tutor
compute()

# --------- The Stack Explained ---------

def greet(name):
    # 'message' is a local variable, stored in the stack
    message = "Hello, " + name
    print(message)
greet('Alice')

# --------- The Heap Explained ---------

class Person:
    def __init__(self, name):
        # 'name' attribute is stored in the heap as part of the object
        self.name = name
person_instance = Person('Bob')

# --------- Stack and Heap in a Finite Space ---------
# Stack allocation (small, short-lived)
def calculate():
    result = 2 + 2
    return result

# Heap allocation (larger, longer-lived)
large_data = [i * 2 for i in range(100000)]

# --------- Values and References in Python ---------

# Value type: Copied when passed to a function
def increment(number):
    number += 1
    return number

# Reference type: The reference is passed, original list can be modified
def append_to_list(lst):
    lst.append(4)

lst = [1, 2, 3]
append_to_list(lst)
number = 10
increment(number)

# --------- Recursion and Stack Overflow in Python ---------

def recursive_function(counter):
    if counter == 0:
        return
    else:
        return recursive_function(counter - 1)
# recursive_function(10000)  # Uncommenting this can cause a stack overflow
recursive_function(5) # This is fine

# --------- Preventing Stack Overflow ---------

import sys
sys.setrecursionlimit(10000)  # Increase the maximum recursion depth

def iterative_function(max_count):
    while max_count > 0:
        max_count -= 1

iterative_function(10000)  # No risk of stack overflow

# --------- Simulating Memory Allocation ---------
# This code can be visualized using Python Tutor to show memory allocation
def compute_squares(numbers):
    squares = [number ** 2 for number in numbers]  # Heap allocation
    return squares
numbers = [1, 2, 3, 4, 5]  # Heap allocation
square_numbers = compute_squares(numbers)

# --------- Analyzing Code for Memory Use ---------
# Analyze the following code for memory allocation:
class DataProcessor:
    def process(self, data):
        # Where is 'processed_data' stored? (Heap)
        processed_data = [d * 2 for d in data]
        return processed_data

processor = DataProcessor()
raw_data = [1, 2, 3, 4, 5]  # How could we free up memory used by 'raw_data'? (Remove references)
processed_data = processor.process(raw_data)  # What is 'processed_data'? (Heap-allocated list)
