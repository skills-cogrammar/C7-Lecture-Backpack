////Strings
const X = "Peter";
const Y = "Jack";
const result = `The names are ${X} and ${Y}`;

let hello = "hello";
console.log(hello[1]); // "e"
console.log(hello.length); // 5
console.log(hello.concat("world")); // helloworld
hello = "hello";
console.log(hello.replace("lo", "ll")); // helll
let sentence = "Another brick in the wall";
console.log(sentence.split(" "));
// ['Another', 'brick', 'in', 'the', 'wall']
console.log(sentence.toLowerCase()); // another brick in the wall
console.log(sentence.toUpperCase()); // ANOTHER BRICK IN THE WALL

let sentence3 = "     Middle     ";
console.log(sentence3.trim()); // Middle

let word4 = "I like Javascript";
console.log(word4.includes("Java")); // true

let word = "Hellooooooo";
console.log(word.substring(2, 5)); // llo
console.log(word.slice(2, 5)); // llo

//// Arrays

// empty array
let colors = [];

// array of strings
let colors2 = ["red", "blue", "green"];

// array with mixed data types
let data = ["name", 1, true];

let even = [2, 4, 6, 8, 10];
console.log("even[0]: ", even[0]); // even[0]:  2
console.log("even[2]: ", even[2]); // even[2]:  6
console.log(even.push(12)); // 6
console.log(even.unshift(0)); // 7
even = [2, 4, 6, 8, 10];
even[0] = 100;
console.log(even); // [100, 4, 6, 8, 10]
// remove one element at the index 2
even = [2, 4, 6, 8, 10];
console.log(even.splice(2, 1)); // [6]
console.log(even); // [2, 4, 8, 10]
console.log(even.length); // 4

let part1 = [2, 3, 5, 7];
let part2 = [2, 4, 6, 8];
// join two arrays
let joined = part1.concat(part2);
console.log(joined);

let languages = ["English", "Japanese", "French", "Spanish"];
// get the index of the first occurrence of "JavaScript"
let index = languages.indexOf("French");
console.log(index);
console.log(languages.includes("English"));

let num = [1, 3, 4, 9, 8];
// get the first even number
let even1 = num.find((x) => x % 2 == 0);
console.log(even1);

let firstEven = num.findIndex((element) => element % 2 !== 0);
console.log("firstEven", firstEven);

num.forEach(function (even) {
  console.log(even * even);
});

console.log(
  "Asc",
  num.sort((a, b) => a - b)
);
console.log(
  "Desc",
  num.sort((a, b) => b - a)
);

let dice = [1, 2, 3, 4, 5, 6];
// create another array by slicing numbers from index 3 to 5
let newArray = dice.slice(3, 6);
console.log("newArray", newArray);

let odd_numbers = [1, 3, 5, 7, 9, 11];
// replace 1 element from index 4 by 13
let removedElement = odd_numbers.splice(4, 1, 13);
console.log("removedElement", removedElement);
console.log("odd_numbers", odd_numbers);

// Output: [ 9 ]
//         [ 2, 3, 5, 7, 13, 11 ]

//// While loops
while (condition) {
  // body of loop
}

// program to display numbers from 1 to 5
// initialize the variable
let laps = 1,
  finish_line = 5;

// while loop from i = 1 to 5
while (laps <= finish_line) {
  console.log(laps);
  laps += 1;
}

// infinite while loop
while (true) {
  // body of loop
}

//// For loops

for (initialExpression; condition; updateExpression) {
  // for loop body
}

const MAX = 5;
// looping from i = 1 to 5
for (let i = 1; i <= MAX; i++) {
  console.log(`Good night`);
}

// infinite for loop
for (let i = 1; i > 0; i++) {
  console.log("I will go onnnnn foreverrrrrrr.....");
}

// program to print the value of i
for (let i = 1; i <= 5; i++) {
  // break condition
  if (i == 3) {
    break;
  }
  console.log(i);
}

for (let i = 1; i <= 5; i++) {
  // condition to continue
  if (i == 3) {
    continue;
  }

  console.log(i);
}

// nested for loops
for (let i = 1; i <= 3; i++) {
  for (let j = 1; j <= 3; j++) {
    console.log(`i = ${i}, j = ${j}`);
  }
}

//// Maps
let m = new Map(); // Create a new, empty map
let n = new Map([
  // A new map initialized with string keys mapped to numbers
  ["one", 1],
  ["two", 2],
]);

let copy = new Map(n); // A new map with the same keys and values as map n
let o = { x: 1, y: 2 }; // An object with two properties
let p = new Map(Object.entries(o)); // Same as new map([["x", 1], ["y", 2]])

let x = new Map(); // Start with an empty map
console.log(x.size); // => 0: empty maps have no keys
x.set("one", 1); // Map the key "one" to the value 1
x.set("two", 2); // And the key "two" to the value 2.
console.log(x.size); // => 2: the map now has two keys
x.get("two"); // => 2: return the value associated with key "two"
x.get("three"); // => undefined: this key is not in the set
x.set("one", true); // Change the value associated with an existing key
console.log(x.size); // => 2: the size doesn't change
console.log(x.has("one")); // => true: the map has a key "one"
console.log(x.has(true)); // => false: the map does not have a key true
x.delete("one"); // => true: the key existed and deletion succeeded
console.log(x.size); // => 1
x.delete("three"); // => false: failed to delete a nonexistent key
x.clear(); // Remove all keys and values from the map

console.log(x.keys()); // => ["x", "y"]: just the keys
console.log(x.values()); // => [1, 2]: just the values
console.log(x.entries()); // => [["x", 1], ["y", 2]]
