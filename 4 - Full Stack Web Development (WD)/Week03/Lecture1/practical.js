// function sum(num1, num2, num3, num4) {
//     console.log(`The sum is: ${num1 + num2 + num3 + num4}`)
// }

// sum(4, 3, 5, 10)

// function sumWithReturn(num1, num2, num3, num4) {
//     // console.log(`The sum is: ${num1 + num2 + num3 + num4}`)
//     let sum = num1+ num2 + num3 + num4
//     return sum;
// }

// let result = sumWithReturn(3,3,3,3);
// console.log(`The result is: ${result}`)

function printHello(){
    console.log("Hello")
}

printHello();

// let username = "Zahir" // Global variable

function a(){
    let username = "Zahir" // Function scope
    console.log(username)
}

function b(){
    console.log(username)
}

a()
// b()

if (true){
 let count = 10   
}

function findCount(){
    console.log(count)
}

// findCount()

function Outer(){ // Container function 
    let a = 10;
    let b = 100;

    function Inner(){ // Nested function
        
        let x = 1;
        let y = 10;
        console.log(a) // Closure
        console.log(b) // Closure
    }
    // Inner()
    return Inner;
}

// Outer()
function writeName(){
    fullName = "Zahir Junejo";
    var fullName;
    console.log(fullName)
}

writeName()