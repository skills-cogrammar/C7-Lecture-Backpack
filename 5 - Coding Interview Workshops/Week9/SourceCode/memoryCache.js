// Implementation of a hash table in JavaScript which will be used to implement a memory cache
// Collision handling will be done using linear probing

// Each element in our array needs to hold a key-value pair
// We create a node class to hold the pair 
// We also implement a mechanism to keep track of whether the node was accessed recently
class Node {
    constructor(key, value, accessed) {
        this.key = key;
        this.value = value;
        this.accessed = accessed;
    }
}

class HashTable {
    // Initialise the Hash Table of arbitary size
    // Use numpy empty array for the associative array
    constructor(capacity = 20) {
        this.capacity = capacity;
        this.size = 0;
        this.buckets = new Array(this.capacity).fill(null);
    }
    
    // JavaScript does not have a built in hash function so 
    // we have to create one ourselves. For this implementation we 
    // add the ascii value of each character in the key.
    // Since this returns integers of arbitray sizes, we 
    // use the mod function to ensure they fit in the array
    _hash(key) {
        let sum = 0;
        let stringKey = String(key);
        for (let i = 0; i < stringKey.length; i++) {
            sum += stringKey.charCodeAt(i);
        }
        return (sum) % this.capacity;
    }
    
    // Return the key of the value that was accessed last 
    // i.e. the item with the lowest access value
    findLastAccessed() {
        let minAccessed = Infinity;
        let minKey = null;

        this.buckets.forEach(
            function (node) {
                if (node.accessed < minAccessed) {
                    minAccessed = node.accessed;
                    minKey = node.key;
                }
            }
        );
            
        return minKey;
    }
    
    // Set a key-value pair in the hash table
    set(key, value, accessed) {
        // Check whether the table is full, if so remove last accessed item
        if (this.size == this.capacity){
            let removeKey = this.findLastAccessed();
            this.remove(removeKey);
        }

        // Hash the key of the pair
        let index = this._hash(key);

        // Check if there is a collision
        if (this.buckets[index] == null) {
            this.buckets[index] = new Node(key, value, accessed);
            this.size += 1;
        } else {
            // If there is a collision find the next empty spot to insert
            index += 1;
            if (index == this.capacity)
                index = 0;

            while (this.buckets[index] != null) {
                index += 1;
                if (index == this.capacity)
                    index = 0;
            }

            this.buckets[index] = new Node(key, value, accessed);
            this.size += 1;
        }
    }

    // Get the value associated with a given key
    get(key, accessed) {
        // Find the index where the pair is stored
        let index = this._hash(key);

        // Check the bucket and retrieve the correct value
        // Return null if the key is not in the hash table
        let node = this.buckets[index];
        if (node == null) {
            return null;
        } else {
            let counter = 1;
            while (node.key != key) {
                // Check whether the whole hash table has been iterated through
                if (counter == this.capacity)
                    return null;
                counter += 1;
                
                // Check whether the end of the table has been reached
                index += 1;
                if (index == this.capacity)
                    index = 0;

                node = this.buckets[index];
                if (node == null)
                    return null;
            }
            node.accessed = accessed;
            return node.value;
        }
    }

    // Remove a pair from the hashtable given the key
    // Return the removed value and null if key isnt found  
    remove(key) {
        // Find the index where the pair is stored
        let index = this._hash(key);

        // Check the bucket and remove the correct node
        // Return null if the key is not in the hash table
        let node = this.buckets[index];
        if (node == null)
            return null;
        else {
            let counter = 1;
            while (node.key != key) {
                // Check whether the whole hash table has been iterated through
                if (counter == this.capacity)
                    return null;
                counter += 1;
                
                // Check whether the end of the table has been reached
                index += 1;
                if (index == this.capacity)
                    index = 0;

                node = this.buckets[index];
                if (node == null)
                    return null;
            }
            
            // Remove the item from the list by setting the element to null
            this.size -= 1;
            this.buckets[index] = null;
            return node.value;
        }
    }
}

class MemoryCache {
    constructor(maxCacheSize = 100) {
        this.maxCacheSize = maxCacheSize;
        this.cache = new HashTable(this.maxCacheSize);
        this.accessCount = 0;
    }

    // Method to read file from disk if not found in cache
    // This is a dummy method for demonstration purposes
    readFromDisk(filename) {
        console.log(`Reading ${filename} data from disk`);
        return `Example data from ${filename}`;
    }
    
    // Method to get data from file given a file name
    // If the file is not in the cache, fetch from disk
    getFile(filename) {
        let data = this.cache.get(filename, this.accessCount);
        
        if (data != null) {
            console.log(`Data fetched from cache : ${data}`);
            this.accessCount += 1;
            return data;
        }
        
        // Fetch data from disk and add to cache
        data = this.readFromDisk(filename);
        this.cache.set(filename, data, this.accessCount);
        this.accessCount += 1;
        return data;
    }
}


// Example cache to test code
let cache = new MemoryCache(2);

// First access - data is read from disk and stored in the cache
console.log(cache.getFile("file1.txt"));

// Second access - data is retrieved from the cache
console.log(cache.getFile("file1.txt"));

// Access a different file - data is read from disk and stored in the cache
console.log(cache.getFile("file2.txt"));

// Access a different file, causing eviction from the cache
console.log(cache.getFile("file3.txt"));

// Access the evicted file - data is read from disk and stored in the cache
console.log(cache.getFile("file1.txt"));

