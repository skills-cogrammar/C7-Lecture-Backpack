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

// function printHello(){
//     console.log("Hello")
// }

// printHello();

// let username = "Zahir" // Global variable

// function a(){
//     let username = "Zahir" // Function scope
//     console.log(username)
// }

// function b(){
//     console.log(username)
// }

// a()
// b()

// if (true){
//  let count = 10   
// }

// function findCount(){
//     console.log(count)
// }

// findCount()

// function Outer(){ // Container function 
//     let a = 10;
//     let b = 100;

//     function Inner(){ // Nested function
        
//         let x = 1;
//         let y = 10;
//         console.log(a) // Closure
//         console.log(b) // Closure
//     }
//     // Inner()
//     return Inner;
// }

// Outer()
// function writeName(){
//     fullName = "Zahir Junejo";
//     var fullName;
//     console.log(fullName)
// }

// writeName()


//arrow function
// let add = (x,y) => {
//     // console.log(x)
//     // console.log(y)
//     return x + y;
// } 

// add(2,3)

//arrow function (even shorter)
// let add = (x,y) => x + y;
// console.log(add(3,5))

function transform(element){
    return element * 2;
}

// const numbers = [1, 2, 3, 4, 5];
// const doubled = numbers.map(num => num * 2);
// console.log(`Original array: ${numbers}`)
// console.log(`Doubled array: ${doubled}`);

// const scores = [80, 90, 60, 45, 75];
// const passed = scores.filter(score => score % 2 != 0);
// console.log(scores)
// console.log(passed);

// const numbers = [1, 2, 3, 4, 5];
// const sum = numbers.reduce((acc, num) => acc + num, 0);
// console.log(sum);

// let twoDimArr = [[2,2],[3,3],[4,4]] // 2 x 3
// let oneDimArr = twoDimArr.reduce((result, arr) => result.concat(arr),[])
// console.log(twoDimArr)
// console.log(oneDimArr)

// function fetchData(callback) {
//     setTimeout(() => {
//       const data = 'Hello Zahir';
//       callback(data);
//     }, 3000);
//   }
  
//   fetchData(data => {
//     console.log(data); 
//   });
  
// document
// .getElementById('myButton')
// .addEventListener('click', () => {
//     console.log('Button clicked!');
//   });
  
// const add = x => x + 100;
// const multiplyByTwo = x => x * 2;

// // // // Compose two functions
// const composedFunction = x => multiplyByTwo(add(x));

// console.log(composedFunction(3));

// let people = ["Zahir", "Liano", "Ronald", "Bongani"]

// let checkUninvited = (arr) => (fn) => {
//     let inviteList = ["Liano", "Ronald", "Bongani"]
//     for(let element of arr){
//         if(!fn(element, inviteList)){
//             return `${element} was not invited to the party.`;
//         }
//     }
// }
// console.log(checkUninvited(people)((x,y) => y.includes(x)))

// let reverseAll = (arr) => (f) => {
//     let namesReversed = []
//     for(let name of arr){
//         namesReversed.push(f(name))
//     }

//     return namesReversed;
// }

// console.log(reverseAll(people)(x => x.split('').reverse().join('')))

// let i = 10;
// let timer = setInterval(()=> {
    
//     console.log(i--);
//     if(i < 0){
//         clearInterval(timer)
//     }
// }, 1000)


