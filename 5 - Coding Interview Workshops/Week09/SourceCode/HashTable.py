# Implementation of a hash table in Python
# Collision handling will be done using chaining
import numpy as np 

# Each element in our array needs to hold a key-value pair
# We create a node class to hold the pair 
# We also implement a linked list for chaining
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    # Initialise the Hash Table of arbitary size
    # Use numpy empty array for the associative array
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.buckets = np.empty(capacity, dtype=Node)
    
    # We will be using the built in hash function
    # Since this returns integers of arbitray sizes, we 
    # use the mod function to ensure they fit in the array
    # 5%6 = 5 (5/6 = 0 r 5), 7%2 = 1 (7/2 = 3 r 1)
    def __hash(self, key):
        return (hash(key)) % self.capacity
    
    # Set a key-value pair in the hash table
    def set(self, key, value):
        # Hash the key of the pair
        index = self.__hash(key)

        # Check if there is a collision
        node = self.buckets[index]
        if (node == None):
            self.buckets[index] = Node(key, value)
            self.size += 1
        else:
            # If there is a collision, check for same key or
            # add to end of linked list and increment size
            print("Collision at position", index)
            while (node.next != None) and (node.key != key):
                node = node.next
            
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)
                self.size += 1

    # Get the value associated with a given key
    def get(self, key):
        # Find the index where the pair is stored
        index = self.__hash(key)

        # Check the bucket and retrieve the correct value
        # Return None if the key is not in the hash table
        node = self.buckets[index]
        if (node == None):
            return None
        else:
            while (node.key != key):
                node = node.next
                if (node == None):
                    return None
            return node.value

    # Remove a pair from the hashtable given the key
    # Return the removed value and None if key isnt found  
    def remove(self, key):
        # Find the index where the pair is stored
        index = self.__hash(key)

        # Check the bucket and remove the correct node
        # Return None if the key is not in the hash table
        node = self.buckets[index]
        prev = None
        if (node == None):
            return None
        else:
            while (node.key != key):
                prev = node
                node = node.next
                if (node == None):
                    return None
            
            # Relink the list if a node is removed midlist
            self.size -= 1
            if prev == None:
                self.buckets[index] = node.next
            else:
                prev.next = node.next

            return node.value

# Example hashtable to test code which stores names and ages
hashtable = HashTable(5)

# Test set 
hashtable.set("Zahra", 23)
print(hashtable.get("Zahra"))

# Test modifiying elements
hashtable.set("Zahra", 24)
print(hashtable.get("Zahra"))

hashtable.set("Anri", 21)
hashtable.set("Jack", 56)
hashtable.set("Amy", 7)
hashtable.set("Thandi", 19)

# Test that element is still in array
print(hashtable.get("Thandi"))

hashtable.set("Thandi", 20)

# Test that element is still in array
print(hashtable.get("Thandi"))

# Test removing elements
hashtable.remove("Zahra")
print(hashtable.get("Zahra"))

# Test that element is still in array
print(hashtable.get("Thandi"))



            


