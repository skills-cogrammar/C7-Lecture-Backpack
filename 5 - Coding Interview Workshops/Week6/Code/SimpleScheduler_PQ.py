# Implementation of a simple task scheduler which uses a PQ
# Use the PrioirityQueue class from the queue module
from queue import PriorityQueue

class SimpleScheduler:

    # Initialise the scheduler which is a priority queue
    def __init__(self):
        self.priorityqueue = PriorityQueue()

    # Add tasks to the scheduler
    # Remember we have to use the inverse priority
    def add_task(self, value, priority):
        self.priorityqueue.put((-1*priority, value))

    # Execute a task from the scheduler
    def execute_task(self):
        if self.priorityqueue.qsize() == 0:
            print("Error: Priority Queue Underflow!")
            return None
        else:
            task = self.priorityqueue.get()
            print("Executing Task: {} \t \
                  Priority: {}".format(task[1], -1*task[0]))
            return task[1]
    
    # Execute all tasks on the scheduler
    def execute_all_tasks(self):
        while self.priorityqueue.qsize() > 0:
            self.execute_task()
        print("All scheduled tasks have been executed")

# Test the scheduler
scheduler = SimpleScheduler()

# Add some tasks to the scheduler
scheduler.add_task("Low Priority Task", 10)
scheduler.add_task("Low Priority Task", 12)
scheduler.add_task("High Priority Task", 90)
scheduler.add_task("Medium Priority Task", 60)
scheduler.add_task("Low Priority Task", 8)
scheduler.add_task("High Priority Task", 90)

# Execute the tasks on the scheduler
scheduler.execute_all_tasks()