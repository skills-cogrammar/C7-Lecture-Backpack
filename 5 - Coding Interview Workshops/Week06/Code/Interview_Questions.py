# Question 1: Implement a stack using a Python list. Include push, pop,
# and is_empty methods.

# class Stack:
#     def __init__(self):
#         self.items = []
#         self.top = 0

#     # push, pop, is_empty

#     # O(1)
#     def push(self, item):
#         self.top += 1
#         self.items.append(item)

#     # LIFO principle
#     # O(1)
#     def pop(self):
#         self.top -= 1
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             # raise IndexError("Cannot pop from an empty stack")
#             print("Cannot pop from an empty stack")

#     def is_empty(self):
#         return self.top == -1
#         # return len(self.items) == 0 # Check if stack is empty

# # test
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.is_empty())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
















# Question 2: Implement a function that checks if a given string of
# parentheses is balanced using a stack (equal number of open and close parentheses).

# (()) = True
# (() = False

def is_balanced(parentheses):
    stack = []

    for char in parentheses:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced("(())"))
print(is_balanced("(()"))








# Question 3: Implement a function called apply_operation that takes a
# function as an argument and returns a new function that applies the
# given function to its argument and doubles the result.


