# Simple priority queue class which uses a list

class PriorityQueue:
    # Initialise the queue by creating an empty list
    # Each element will be a pair of values (tuple)
    def __init__(self):
        self.pqueue = []

    # Add an element to the end of the queue
    # Sort by priority to queue by priority
    def enqueue(self, value, priority):
        self.pqueue.append((priority, value))
        self.pqueue.sort()

    # Remove the element with the highest priority
    # The element would be at the end of list but
    # the beginning of our queue
    def dequeue(self):
        if len(self.pqueue) == 0:
            print("Error: Priority Queue Underflow!")
            return None
        else:
            return self.pqueue.pop()[1]
    

# Create a priority queue to test the class
pqueue = PriorityQueue()

# Check underflow error
pqueue.dequeue()

# Add some elements to the priority queue
pqueue.enqueue(1, 90)
pqueue.enqueue(2, 100)
pqueue.enqueue(945, 95)

# Remove an element from the priority queue
popped = pqueue.dequeue()
print("Dequeued element: {}".format(popped))
