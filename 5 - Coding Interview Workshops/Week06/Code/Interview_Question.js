// Question 1: Implement a stack using a Python list. Include push, pop,
// and is_empty methods.

// class Stack
// {
//     constructor(){        
//         this.items = [];    
//     }

//     push(element){
//         this.items.push(element);
//     }

//     pop(){
//         if (this.isEmpty()){
//             console.log("Cannot pop from an empty stack")
//             return
//         }            
        
//         return this.items.pop()
//     }

//     isEmpty(){
//         return this.items.length == 0
//     }
// }

// stack = new Stack()
// stack.push(1)
// stack.push(2)
// stack.push(3)

// console.log(stack.isEmpty())

// console.log(stack.pop())
// console.log(stack.pop())
// console.log(stack.pop())
// console.log(stack.pop())


// Question 2: Implement a function that checks if a given string of
// parentheses is balanced using a stack (equal number of open and close parentheses).

// (()) = True
// (() = False


function isBalanced(parentheses){
    let stack = []
    
    for (const char of parentheses) {        
        if (char == '('){
            stack.push(char)
        }
        else{            
            if (!stack)
                return false

            stack.pop()
        }
    }

    return stack.length
}

console.log(isBalanced("(())"))
console.log(isBalanced("(()"))
