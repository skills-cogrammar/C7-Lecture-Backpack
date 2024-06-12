// Implementation of a hash table in JavaScript
// Collision handling will be done using chaining

// Each element in our array needs to hold a key-value pair
// We create a node class to hold the pair 
// We also implement a linked list for chaining
class Node {
    constructor (key, value){
        this.key = key;
        this.value = value;
        this.next = null;
    }
}

class HashTable {
    // Initialise the Hash Table of arbitary size
    // Use an empty array of set size for the associative array
    constructor (capacity = 20) {
        this.capacity = capacity;
        this.size = 0;
        this.buckets = new Array(this.capacity).fill(null);
    }
    
    // JavaScript does not have a built in hash function so 
    // we have to create one ourselves. For this implementation we 
    // add the ascii value of each character in the key.
    // Since this returns integers of arbitray sizes, we 
    // use the mod function to ensure they fit in the array
    // 5%6 = 5 (5/6 = 0 r 5), 7%2 = 1 (7/2 = 3 r 1)
    _hash(key) {
        let sum = 0;
        let stringKey = String(key);
        for (let i = 0; i < stringKey.length; i++) {
            sum += stringKey.charCodeAt(i);
        }
        return (sum) % this.capacity;
    }
    
    // Set a key-value pair in the hash table
    set(key, value) {
        // Hash the key of the pair
        let index = this._hash(key);

        // Check if there is a collision
        let node = this.buckets[index];
        if (node == null) {
            this.buckets[index] = new Node(key, value);
            this.size += 1;
        } else {
            // If there is a collision, check for same key or
            // add to end of linked list and increment size
            console.log(`Collision at position ${index}`);
            while ((node.next != null) && (node.key != key))
                node = node.next;
            
            if (node.key == key)
                node.value = value;
            else {
                node.next = new Node(key, value);
                this.size += 1;
            }
        }
    }

    // Get the value associated with a given key
    get(key) {
        // Find the index where the pair is stored
        let index = this._hash(key);

        // Check the bucket and retrieve the correct value
        // Return null if the key is not in the hash table
        let node = this.buckets[index];
        if (node == null)
            return null;
        else {
            while (node.key != key) {
                node = node.next;
                if (node == null)
                    return null;
            }
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
        let prev = null;
        if (node == null)
            return null;
        else {
            while (node.key != key) {
                prev = node;
                node = node.next;
                if (node == null)
                    return null;
            }
            // Relink the list if a node is removed midlist
            this.size -= 1;
            if (prev == null)
                this.buckets[index] = node.next;
            else
                prev.next = node.next;

            return node.value;
        }
    }

}
// Example hashtable to test code which stores names and ages
let hashtable = new HashTable(5);

// Test set 
hashtable.set("Zahra", 23);
console.log(hashtable.get("Zahra"));

// Test modifiying elements
hashtable.set("Zahra", 24);
console.log(hashtable.get("Zahra"));

hashtable.set("Anri", 21);
hashtable.set("Jack", 56);
hashtable.set("Amy", 7);
hashtable.set("Thandi", 19);
console.table(hashtable.buckets);

// Test that element is still in array
console.log(hashtable.get("Thandi"));

hashtable.set("Thandi", 20);

// Test that element is still in array
console.log(hashtable.get("Thandi"));

// Test removing elements
hashtable.remove("Zahra");
console.log(hashtable.get("Zahra"));

// Test that element is still in array
console.log(hashtable.get("Thandi"));