// let a = Number(prompt("Enter a: "));
// let b = Number(prompt("Enter b: "));
// console.log(`${a} + ${b} = ${a + b}`);
////Strings
// const X = "Zahir";
// const Y = 'Jack';
// const result = `The names are ${X} and ${Y}`;
// console.log(result);

// A string is an array of characters
// let hello = "hello";
// console.log(hello[3]);
// console.log(hello.length);
// console.log(hello.concat("world"));
// hello = "hello";
// console.log(hello.replace("lo", "zahir"));

// let sentence = "Another brick in the wall";
// console.log(sentence.split(" "));
// console.log(sentence.toLowerCase());
// console.log(sentence.toUpperCase());

// let sentence3 = "     Eye of the tiger     ";
// console.log(sentence3)
// console.log(sentence3.trim());

// let word4 = "I like Javascript";
// console.log("word4.includes:", word4.includes("script"));

// let word = "Hellooooooo";
// First argument is inclusive. Second arg is exclusive.
// console.log("Slice: ", word.slice(2, 5));

// //// Arrays

// // empty array
// let colors = [];

// // array of strings
// let colors2 = ["red", "blue", "green"];

// // array with mixed data types
// let data = ["name", 1, true];

// Multidim array
// let table = [
//     ["zahir", 1],
//     ["john", 2],
//     ["jax", 3]
// ]

// console.log(table[1])
// console.log(table[1][0])

let even = [2, 4, 6, 8, 10];
// console.log(even[2]);

// console.log(even.push(12));
// console.log(even)
// Inserts new elements at the start of an array,
// and returns the new length of the array.
// console.log(even.unshift(1000));
// console.log(even)

// even = [2, 4, 6, 8, 10];
// even[0] = 100;
// console.log(even);

// even = [2, 4, 6, 8, 10];
// console.log(even.splice(2, 1));
// console.log(even); // [2, 4, 8, 10]
// console.log(even.length); // 4

// let part1 = [2, 3, 5, 7];
// let part2 = [2, 4, 6, 8];
// // join two arrays
// let joined = part1.concat(part2);
// console.log(joined);

let languages = ["English", "Japanese", "French", "Spanish"];
// let index = languages.indexOf("Japanese");
// console.log(index);

// console.log(languages.includes("English"));

let num = [1, 3, 4, 9, 8];
// get the first even number
// let even1 = num.find((x) => x % 2 != 0);
// console.log(even1);

// num.forEach(function (even) {
//   console.log(even * even * even);
// });

// console.log(
//   "Asc",
//   num.sort((a, b) => a - b)
// );
// console.log(
//   "Desc",
//   num.sort((a, b) => b - a)
// );

// let dice = [1, 2, 3, 4, 5, 6];
//  create another array by slicing numbers
//  from index a to b
// let newArray = dice.slice(1, 4);
// console.log("newArray", newArray);

// let odd_numbers = [1, 3, 5, 7, 9, 11];
// replace 1 element from index 4 by 13
// let removedElement = odd_numbers.splice(4, 1, 13);
// console.log("removedElement", removedElement);
// console.log("odd_numbers", odd_numbers);

// //// While loops
// while (condition) {
//   // body of loop
// }

// // program to display numbers from 1 to 5
// // initialize the variable
let laps = 1,
  finish_line = 5;

// // while loop from i = 1 to 5
// while (laps <= finish_line) {
//   console.log(laps);
//   laps += 1;
// }

// // infinite while loop
// while (true) {
//   // body of loop
// }

// //// For loops

// for (initialExpression; condition; updateExpression) {
//   // for loop body
// }

// const MAX = 5;
// // looping from i = 1 to 5
// for (let i = 1; i <= MAX; i++) {
//   console.log(`Good night`);
// }

// // infinite for loop
// for (let i = 1; i > 0; i++) {
//   console.log("I will go onnnnn foreverrrrrrr.....");
// }

// // program to print the value of i
// for (let i = 1; i <= 5; i++) {
//   // break condition
//   if (i == 3) {
//     break;
//   }
//   console.log(i);
// }

// for (let i = 1; i <= 5; i++) {
//   // condition to continue
//   if (i == 3) {
//     continue;
//   }

//   console.log(i);
// }

// // nested for loops
// for (let i = 1; i <= 3; i++) {
//   for (let j = 1; j <= 3; j++) {
//     console.log(`i = ${i}, j = ${j}`);
//   }
// }

// //// Maps
// let m = new Map(); // Create a new, empty map

let x = new Map(); // Start with an empty map
// console.log(x.size); // => 0: empty maps have no keys
// x.set("one", 1); // Map the key "one" to the value 1
// x.set("two", 1000); // And the key "two" to the value 2.
// console.log(x.size); // => 2: the map now has two keys
// console.log(x.get("two")); // => 2: return the value associated with key "two"
// console.log(x.get("three")); // => undefined: this key is not in the set
// console.log(x)
// x.set("one", true); // Change the value associated with an existing key
// console.log(x)
// console.log(x.has("one")); // => true: the map has a key "one"
// console.log(x.has("momomomomomo")); // => false: the map does not have a key true

// console.log("Size before delete: ", x.size);
// x.delete("one"); // => true: the key existed and deletion succeeded
// console.log("Size after delete: ", x.size); // => 1
// console.log(x)
// x.clear(); // Remove all keys and values from the map
// console.log(x)
// console.log(x.keys()); // => ["x", "y"]: just the keys
// console.log(x.values()); // => [1, 2]: just the values
// console.log(x.entries()); // => [["x", 1], ["y", 2]]
