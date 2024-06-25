class Node
{
    constructor(value){
        this.value = value;
        this.next = null
    }
}

class Stack
{
    head = null
    
    constructor(){
    }

    push(value){        
        let node = new Node(value)        

        if (this.head === null){
            this.head = node;
            return;        
        }
        
        node.next = this.head;        
        this.head = node
    }

    pop(){
        if (this.head === null){
            return null;
        }

        let value = this.head.value;
        this.head = this.head.next;
        return value;
    }

    getLinkedList(){
        return this.head;
    }    
}