class LinkedNode
{
    constructor(value)
    {
        this.value = value;
        this.next = null;
    }

    /**
     * Add a new value to the linked list
     * @param {Number} value value to be added to the linked list
     */
    add(value){
        // Set the head node to the current node 
        // `this` will give us the variable that the user is calling the method from
        let current_node = this;

        // Traverse to the end of the linked list to find the tail node
        while (current_node.next !== null){
            current_node = current_node.next;                    
        }

        // Once we are at the tail, we can create a new node and 
        // add it to the previous tail.
        let new_node = new LinkedNode(value);
        current_node.next = new_node;
    }

    /**
     * Revese a linked list
     * @returns new head node of the reversed linked list
     */
    reverse(){
        let prev = null; // we haven't looked at any other nodes yet
        let current_node = this; // get the head node
        
        // While we haven't looked at the current node        
        while (current_node !== null){   
            // Store the next node because we are going to overwrite it                     
            let next = current_node.next;

            // Set the next node to the previous node and set the current node as the new
            // previous node
            current_node.next = prev;
            prev = current_node;

            // Go to the next node
            current_node = next            
        }
        
        // Since the last value of current_node is null the loop will exit
        // prev will have the value of the tail node which will be our new head node
        return prev
    }

    print(){
        let current_node = this;
        let values = [];

        while (current_node !== null){
            values.push(current_node.value);
            current_node = current_node.next;
        }

        console.log(`Linked List: ${values.join(" -> ")}`);    
    }
}


class Stack
{
    head = null
    size = 0
    
    constructor(){
    }

    push(value){        
        // Create the new node to be added to the stack
        let node = new LinkedNode(value)        

        // check if the head is null, if so, the new node becomes the head
        if (this.head === null){
            this.head = node;
            return;        
        }
        
        // If there is already a head, 
        // Set the current head to the new nodes next
        // Set the new node to the head
        node.next = this.head;        
        this.head = node
    }

    pop(){
        // If there are no values, return null
        // (Should actually be an error)
        if (this.head === null){
            return null;
        }


        // Get the value from the old head
        // set the head to the next node
        // return the value from the old head
        let value = this.head.value;
        this.head = this.head.next;
        return value;
    }

    getLinkedList(){
        // The head node indicates the start of our linked list
        return this.head;
    }    
}

/**
 * Add two numbers represented by linked lists
 * @param {LinkedNode} numOne First Number
 * @param {LinkedNode} numTwo Second number
 */
function addition(numOne, numTwo){
    // reverse both linked lists
    numOne = numOne.reverse()
    numTwo = numTwo.reverse()

    // Set up the stack that will store our output
    let finalResult = new Stack()

    // Set the carry variable 
    // that keeps track of any values that need to 
    // be carried over to the next operation
    let carry = 0;

    // Uses truthy and falsey values to determine if there 
    // are values in either of our variables
    // if all 3 are falsy, we exit the loop
    while (numOne || numTwo || carry){
        // Add any values that need to be carried over to the sum        
        let sum = carry

        // check if there are any values in the numOne 
        // if there are, add the value to the sum and go to the next node
        if (numOne){
            sum += numOne.value
            numOne = numOne.next        
        }

        // Check if there are any values in the numTwo
        // if there are, add the value to the sum and go to the next node
        if (numTwo){
            sum += numTwo.value
            numTwo = numTwo.next
        }

        // Get the numbers that need to be carried over 
        // Create a new node in the stack that contains the unit
        carry = parseInt(sum / 10)
        finalResult.push(sum % 10)
    }

    return finalResult.getLinkedList()
}

let numberOne = new LinkedNode(7)
numberOne.add(2)
numberOne.add(4)
numberOne.add(3)

let numberTwo = new LinkedNode(5)
numberTwo.add(6)
numberTwo.add(4)

let result = addition(numberOne, numberTwo);
result.print()