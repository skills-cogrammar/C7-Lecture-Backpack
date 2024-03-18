let a = 10;
let b = 6;
let total = a + b;
console.log(total);

let caught = 5;
let sum = 5 + 5;
console.log(sum); // 10
console.log("Value of sum: ", sum); // Value of sum: 10

let ten = 10;
console.log(ten * ten);
// Output: 100

let mood = "light";
console.log(mood);
// light
mood = "dark";
console.log(mood);
// dark

let count;
console.log(count);
// undefined

let one = 1,
  two = 2;
console.log(one + two);
// 3

const PI = 3.14;
// PI = 2.2; // You cannot reassign a constant
// console.log(PI);

let temperature = 10.6;
if (temperature < 20) {
  console.log("Yikes, it's too cold here.");
} else {
  console.log("Eh, I can survive.");
}

// if (num < 10) {
//   console.log("Small");
// } else if (num < 100) {
//   console.log("Medium");
// } else {
//   console.log("Large");
// }

// It's a green hollow where a river sings

/*
  I first found this number scrawled on the back of an old
  notebook. Since then, it has often dropped by, showing up in
  phone numbers and the serial numbers of products that I've
  bought. It obviously likes me, so I've decided to keep it.
*/

console.log(13);
console.log(9.81);
console.log(2.998e8);

console.log(100 + 4);
console.log(4 * 11);
console.log(100 - 10);
console.log(100 / 10);

console.log(314 % 100); // 14
console.log(144 % 12); // 0

console.log("The quick brown fox\njumped over the lazy dog"); // new line
console.log("The quick brown fox\tjumped over the lazy dog"); // tab

console.log(`The quick brown fox
              jumped over the lazy dog.`);

console.log(true);
console.log(false);

console.log("Comparison");
console.log(3 > 2); // true
console.log(3 < 2); // false
console.log(4 >= 4); // true
console.log(4 <= 5); // true
console.log(40 == 40); // true
console.log(100 != 100); // false

console.log(true && false); // false
console.log(true && true); // true
console.log(false || true); // true
console.log(false || false); // false
console.log(!true); // false
console.log(!false); // true

// Stack trace example
// function woof() {
//   console.log(barry);
// }

// function foo() {
//   woof();
// }

// function bar() {
//   foo();
// }

// bar();
