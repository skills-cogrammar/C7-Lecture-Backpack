// Simple stack class with the push and pop functions defined
class Stack {
  // Initialise the stack by creating an array of fixed size 
  // and a top pointer 
  constructor(max) {
      this.max_size = max;
      this.stack = new Array(max).fill(null);
      this.top = -1;
  }

  // Push an element to the stack
  // Display a stack overflow error if the stack is full
  push(value) {
      if (this.top === this.max_size - 1) {
          console.log("Error: Stack Overflow!");
          return;
      }
      
      this.top += 1;
      this.stack[this.top] = value;
  }

  // Pop an element from the stack
  // Display a stack underflow error if the stack is empty
  pop() {
      if (this.top === -1) {
          console.log("Error: Stack Underflow!");
          return;
      }

      const removed = this.stack[this.top];
      this.top -= 1;
      return removed;
  }
}

// Create a stack to test the class
const stack = new Stack(10);

// Test the underflow error
stack.pop();

// Add some elements to the stack
stack.push(2);
stack.push(13);

// Remove an element from the stack
stack.pop();

