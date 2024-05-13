let a = 100;
let b = 600;
let doorOpen = true;
let firstName = "Zahir";
console.log(a);
console.log(b);
console.log(doorOpen);
console.log(firstName);
let total = a+b;
// let total = a + b + 799 + a;
console.log(total);
console.log(b - a)
console.log(a * b * b * 100);
console.log(a / b)
console.log(a % 2) // modulo
console.log(13 / 2)
console.log(13 % 2)

let a2 = 1;
a2 += 100; // a2 = a2 + 100
console.log("a2", a2)
a2++ // ++ increment
console.log(a2) 
a2--; // -- decrement
console.log(a2)
let caught = 5;
let sum = 5 + 5;
console.log(sum); // 10
console.log("Value of sum: ", sum); // Value of sum: 10

// let ten = 10;
// console.log(ten * ten);
// Output: 100

// let carName = "Tesla";
// console.log(carName);
// carName = "Toyota";
// console.log(carName);
// dark

// let count;
// console.log(count);
// undefined

// let one = 1,
//   two = 2;
// console.log(one + two);
// 3
// let firstName = "Zahir", lastName = "Junejo";
// console.log(`${firstName} ${lastName}`)

// const PI = 3.14;
// PI = 2.2; // You cannot reassign a constant
// console.log(PI);


// let temperature = 200;

// if (condition) {
//   // code block
// }
// console.log(temperature < 20)
// if (temperature < 20) {
//   console.log("Yikes, it's too cold here.");
// } else {
//   console.log("Eh, I can survive.");
// }
let num = 900, num1 = 300, num2 = 15, num3 = 20;

// if (num < 10) {
//   console.log("Small");
// } else if (num < 100) {
//   console.log("Medium");
// } else {
//   console.log("Large");
// }

// console.log(num < 1000 || num1 > 200)
// if(num < 1000 || num1 > 200){
//  console.log("Helloooo")
// }
// console.log(num < 1000 && num1 > 200)
// if(num < 1000 && num1 > 200){
//   console.log("Helloooo111111")
// }
// It's a green hollow where a river sings (ctrl + /)

/*
  I first found this number scrawled on the back of an old
  notebook. Since then, it has often dropped by, showing up in
  phone numbers and the serial numbers of products that I've
  bought. It obviously likes me, so I've decided to keep it.
*/

/*
  the quick brown fox
  jumped over the lazy
  dog
*/

// console.log(13);
// console.log(9.81);
// console.log(2.998e8);

// console.log(100 + 4);
// console.log(4 * 11);
// console.log(100 - 10);
// console.log(100 / 10);

// console.log(314 % 100); // 14
// console.log(144 % 12); // 0

// console.log("The quick brown fox\njumped over the lazy dog"); // new line
// console.log("The quick \t brown fox\tjumped over \t the lazy dog"); // tab

// console.log(`The quick brown fox
//               jumped over the lazy dog.`);

// console.log(`The value of x is: ${true}`);
// console.log(`The sum of prime numbers is: ${3 + 5 + 7 + 13}`)
// console.log(true);

// console.log("Comparison");
// console.log(`3 > 2 is ${3 > 2}`); // true
// console.log(`3 < 2 is ${3 < 2}`); // false
// console.log(`4 >= 4 is ${4 >= 4}`); // true
// console.log(`4 <= 5 is ${4 <= 5}`); // true
// console.log(`40 == 40 is ${40 == 40}`); // true
// console.log(`100 != 100 is ${100 != 100}`); // false

// console.log(true && false); // false
// console.log(true && true); // true
// console.log(false || true); // true
// console.log(false || false); // false
// console.log(`!true is ${!true}`); // false
// console.log(`!false is ${!false}`); // true

// Stack trace example
function woof() {
  console.log(barry);
}

function foo() {
  woof();
}

function bar() {
  foo();
}

bar();
