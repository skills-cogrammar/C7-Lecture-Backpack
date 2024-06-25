# Implementation of a simple task scheduler which uses a stack
# Use the deque module to avoid Stack Overflow Errors
from collections import deque

class SimpleScheduler:

    # Initialise the scheduler which is a stack
    def __init__(self):
        self.stack = deque()

    # Add tasks to the scheduler
    def add_task(self, value):
        self.stack.append(value)

    # Execute a task from the scheduler
    def execute_task(self):
        if len(self.stack) == 0:
            print("Error: Stack Underflow!")
            return None
        else:
            task = self.stack.pop()
            print("Executing Task: {}".format(task))
            return task
    
    # Execute all tasks on the scheduler
    def execute_all_tasks(self):
        while len(self.stack) > 0:
            self.execute_task()
        print("All scheduled tasks have been executed")

# Test the scheduler
scheduler = SimpleScheduler()

# Add some tasks to the scheduler
scheduler.add_task("Low Priority Task")
scheduler.add_task("Low Priority Task")
scheduler.add_task("High Priority Task")
scheduler.add_task("Medium Priority Task")
scheduler.add_task("Low Priority Task")
scheduler.add_task("High Priority Task")

# Execute the tasks on the scheduler
scheduler.execute_all_tasks()