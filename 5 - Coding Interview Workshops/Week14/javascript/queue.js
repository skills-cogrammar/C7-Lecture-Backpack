class Node
{
    constructor(value){
        this.value = value;
        this.next = null
    }
}

class Queue
{
    head = null
    tail = null
    size = 0
    
    constructor(){
    }

    enqueue(value){        
        const newNode = new Node(value);

        if (this.isEmpty()){
            this.head = this.tail  = newNode;
            this.size++;
            return;
        }

        this.tail.next = newNode;
        this.tail = newNode;
        this.size++;    
    }

    dequeue(){
        if (this.isEmpty()){
            return null;
        }

        let value = this.head.value;
        this.head = this.head.next;
        this.size--;    

        return value
    }

    isEmpty(){
        return this.size === 0    
    }

    getLinkedList(){
        return this.head;
    }
}