//function
// function add(x,y){
//  return x + y;
// }

//arrow function
// let add = (x,y) => {
//     return x + y;
// } 

//arrow function (even shorter)
// let add = (x,y) => x + y;
// console.log(add(3,5))

function transform(element){
    return element * 2;
}

const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
console.log(`Original array: ${numbers}`)
console.log(`Doubled array: ${doubled}`);

const scores = [80, 90, 60, 45, 75];
const passed = scores.filter(score => score % 2 == 0);
console.log(scores)
console.log(passed);

// const numbers = [1, 2, 3, 4, 5];
// const sum = numbers.reduce((acc, num) => acc + num, 0);
// console.log(sum);

// let twoDimArr = [[2,2],[3,3],[4,4]]
// let oneDimArr = twoDimArr.reduce((result, arr) => result.concat(arr),[])
// console.log(twoDimArr)
// console.log(oneDimArr)



// function fetchData(f) {
//     setTimeout(() => {
//       const data = 'Hello Zahir';
//       f(data);
//     }, 3000);
//   }
  
//   fetchData(data => {
//     console.log(data); 
//   });
  
// document
// .getElementById('myButton')
// .addEventListener('click',() => {
//     console.log('Button clicked!');
//   });
  
// const add = x => x + 100;
// const multiplyByTwo = x => x * 2;

// // // Compose two functions
// const composedFunction = x => multiplyByTwo(add(x));

// console.log(composedFunction(3));

let people = ["Zahir", "Liano", "Ronald", "Bongani"]
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

let i = 5;
let timer = setInterval(()=> {
    
    console.log(i--);
    if(i < 0){
        clearInterval(timer)
    }
}, 1000)
