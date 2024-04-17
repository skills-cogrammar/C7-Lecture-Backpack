# Simple stack class with the push and pop functions defined
class Stack:
    # Initialise the stack by creating an array of fixed size 
    # and a top pointer 
    def __init__(self, max):
        self.max_size = max
        self.stack = [None] * max
        self.top = -1

    # Push an element to the stack
    # Display a stack overflow error if the stack is full
    def push(self, value):
        if self.top == self.max_size-1:
            print("Error: Stack Overflow!")
            return
        
        self.top += 1
        self.stack[self.top] = value

    # Pop an element from the stack
    # Display a stack underflow error if the stack is empty
    def pop(self):
        if self.top == -1:
            print("Error: Stack Underflow!")
            return

        removed = self.stack[self.top]
        self.top -= 1
        return removed


# Create a stack to test the class
stack = Stack(10)

# Test the underflow error
stack.pop()

# Add some elements to the stack
stack.push(2)
stack.push(13)

# Remove an element from the stack
stack.pop()
