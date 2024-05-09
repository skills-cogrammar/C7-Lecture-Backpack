# Implementation of a hash table in Python which will be used to implement a memory cache
# Collision handling will be done using linear probing
import numpy as np 

# Each element in our array needs to hold a key-value pair
# We create a node class to hold the pair 
# We also implement a mechanism to keep track of whether the node was accessed recently
class Node:
    def __init__(self, key, value, accessed):
        self.key = key
        self.value = value
        self.accessed = accessed

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
    def hash(self, key):
        return hash(key) % self.capacity
    
    # Return the key of the value that was accessed last 
    # i.e. the item with the lowest access value
    def find_last_accessed(self):
        min_accessed = np.Infinity
        min_key = None
        for node in self.buckets:
            if (node.accessed < min_accessed):
                min_accessed = node.accessed
                min_key = node.key
        return min_key
    
    # Set a key-value pair in the hash table
    def set(self, key, value, accessed):
        # Check whether the table is full, if so remove last accessed item
        if (self.size == self.capacity):
            remove_key = self.find_last_accessed()
            self.remove(remove_key)

        # Hash the key of the pair
        index = self.hash(key)

        # Check if there is a collision
        if (self.buckets[index] == None):
            self.buckets[index] = Node(key, value, accessed)
            self.size += 1
        else:
            # If there is a collision find the next empty spot to insert
            index += 1
            if (index == self.capacity):
                index = 0

            while (self.buckets[index] != None):
                index += 1
                if (index == self.capacity):
                    index = 0

            self.buckets[index] = Node(key, value, accessed)
            self.size += 1

    # Get the value associated with a given key
    def get(self, key, accessed):
        # Find the index where the pair is stored
        index = self.hash(key)

        # Check the bucket and retrieve the correct value
        # Return None if the key is not in the hash table
        node = self.buckets[index]
        if (node == None):
            return None
        else:
            counter = 1
            while (node.key != key):
                # Check whether the whole hash table has been iterated through
                if counter == self.capacity:
                    return None
                counter += 1
                
                # Check whether the end of the table has been reached
                index += 1
                if index == self.capacity:
                    index = 0 

                node = self.buckets[index]
                if (node == None):
                    return None
            node.accessed = accessed
            return node.value

    # Remove a pair from the hashtable given the key
    # Return the removed value and None if key isnt found  
    def remove(self, key):
        # Find the index where the pair is stored
        index = self.hash(key)

        # Check the bucket and remove the correct node
        # Return None if the key is not in the hash table
        node = self.buckets[index]
        if (node == None):
            return None
        else:
            counter = 1
            while (node.key != key):
                # Check whether the whole hash table has been iterated through
                if counter == self.capacity:
                    return None
                counter += 1
                
                # Check whether the end of the table has been reached
                index += 1
                if index == self.capacity:
                    index = 0 

                node = self.buckets[index]
                if (node == None):
                    return None
            
            # Remove the item from the list by setting the element to None
            self.size -= 1
            self.buckets[index] = None
            return node.value

class MemoryCache:
    def __init__(self, max_cache_size = 100):
        self.max_cache_size = max_cache_size
        self.cache = HashTable(self.max_cache_size)
        self.accessCount = 0

    # Method to read file from disk if not found in cache
    # This is a dummy method for demonstration purposes
    def read_from_disk(self, filename):
        print("Reading {} data from disk".format(filename))
        return "Example data from {}".format(filename)
    
    # Method to get data from file given a file name
    # If the file is not in the cache, fetch from disk
    def get_file(self, filename):
        data = self.cache.get(filename, self.accessCount)
        
        if data is not None:
            print("Data fetched from cache : {}".format(data))
            self.accessCount += 1
            return data
        
        # Fetch data from disk and add to cache
        data = self.read_from_disk(filename)
        self.cache.set(filename, data, self.accessCount)
        self.accessCount += 1
        return data


# Example cache to test code
cache = MemoryCache(2)

# First access - data is read from disk and stored in the cache
print(cache.get_file("file1.txt"))

# Second access - data is retrieved from the cache
print(cache.get_file("file1.txt"))

# Access a different file - data is read from disk and stored in the cache
print(cache.get_file("file2.txt"))

# Access a different file, causing eviction from the cache
print(cache.get_file("file3.txt"))

# Access the evicted file - data is read from disk and stored in the cache
print(cache.get_file("file1.txt"))

