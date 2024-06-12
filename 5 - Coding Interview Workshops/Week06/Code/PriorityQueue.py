# Simple priority queue class which uses the queue module
import queue

class PriorityQueue:
    # Initialise the PQ with an instance of the PQ class
    # A PQ of fixed length can be created as well
    def __init__(self):
        self.pqueue = queue.PriorityQueue()

    # Insert an element into the PQ based on its priority
    # This PQ gives the lowest values the highest priority
    # We change the sign of the priorities to fit our need
    def enqueue(self, value, priority):
        self.pqueue.put((-1*priority, value))

    # Remove the element with the highest priority 
    def dequeue(self):
        if self.pqueue.qsize() == 0:
            print("Error: Priority Queue Underflow!")
            return None
        else:
            return self.pqueue.get()[1]
    
# Create a PQ to test the class
pqueue = PriorityQueue()

# Check underflow error
pqueue.dequeue()

# Add some elements to the PQ
pqueue.enqueue(1, 90)
pqueue.enqueue(2, 100)
pqueue.enqueue(945, 95)

# Remove an element from the PQ
popped = pqueue.dequeue()
print("Dequeued element: {}".format(popped))