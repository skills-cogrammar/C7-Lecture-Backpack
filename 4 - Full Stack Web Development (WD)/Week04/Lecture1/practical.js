// Creating an object
// Object literal
// let person = {
//     name: "John Doe",
//     age: 30,
//     city: "New York"
// };

// let vehicle = {
//     no_of_wheels: 4,
//     has_stereo: true,
//     manufacturer_name: "Tesla"
// }

class Animal {
    constructor (name, noLegs) {
        this.name = name;
        this.noLegs = noLegs;
    }
}

class Mammals extends Animal {
    constructor (name, noLegs, colourOfFur, gestationPeriod) {
        super(name, noLegs);
        this.colourOfFur = colourOfFur;
        this.gestationPeriod = gestationPeriod;
    }
}

let animal = new Animal("Snake", 0);
let mammal = new Mammals("Zebra", 4, "Black and White", 8);
let mammal2 = new Mammals("Dolphin", 0);

console.log(animal.name);
console.log(mammal.name);
console.log(mammal2.name);


// Creating objects and setting prototypes
let parent = {
    greet: function() {
        return "Hello";
    }
};

let child = Object.create(parent); // Inherit from parent prototype
// // let child = null;
console.log(child.greet()); // Output: "Hello"

// Defining a class
// class Person {
//     constructor(name, age, gender) {
//         this.name = name;
//         this.age = age;
//         this.gender = gender;
//     }
//     greet() {
//         return `Hello, my name is ${this.name} and I'm ${this.age} years old.`;
//     }

//     sayhi(name){
//         return `Hi, ${name}`;
//     }


// }

// // Creating an instance of the class
// let person1 = new Person("Alice", 25, "Female");
// console.log(person1.sayhi("Zahir"));

// Constructor function
function Car(make, model) {
    this.make = make;
    this.model = model;
}

// Creating an instance using the constructor function
let car1 = new Car("Toyota", "Camry");
console.log(car1.make);

// Converting JavaScript object to JSON
let person = {
    name: "John Doe",
    age: 30,
    city: "New York"
};
console.log(person)
let jsonStr = JSON.stringify(person);
console.log(jsonStr);

// Parsing JSON back to JavaScript object
let person2 = JSON.parse(jsonStr);
console.log(person2.name);
console.log(typeof jsonStr)
console.log(typeof person)

// Prototypal inheritance
// let parent = {
//     greet: function() {
//         return "Hello";
//     }
// };

// let child = Object.create(parent);
// console.log(child.greet()); // Output: "Hello"


// Object methods
// let person = {
//     name: "John Doe",
//     greet: function() {
//         return `Hello, my name is ${this.name}.`;
//     }
// };

// console.log(person.greet()); // Output: "Hello, my name is John Doe."

// Understanding 'this'
// let person = {
//     name: "John Doe",
//     greet: function() {
//         return `Hello, my name is ${this.name}.`;
//     }
// };

// let anotherGreet = person.greet;
// console.log(anotherGreet()); // Output: "Hello, my name is undefined."

// Property descriptors
// let obj = {
//     name: "John"
// };

// let descriptor = Object.getOwnPropertyDescriptor(obj, "name");
// console.log(descriptor); // Output: {value: "John", writable: true, enumerable: true, configurable: true}

// Accessor properties
// let obj = {
//     _name: "John",
//     get name() {
//         return this._name.toUpperCase();
//     },
//     set name(value) {
//         this._name = value;
//     }
// };

// obj.name = "Alice";
// console.log(obj.name); // Output: "ALICE"


// Iterating over object properties
// let obj = {
//     name: "John",
//     age: 30,
//     city: "New York"
// };

// // Using for...in loop
// for (let key in obj) {
//     console.log(`${key}: ${obj[key]}`);
// }

// // Using Object.keys()
// let keys = Object.keys(obj);
// console.log(keys); // Output: ["name", "age", "city"]
// console.log(Object.values(obj))
// Spread syntax for objects

// let obj1 = { name: "John" };
// let obj2 = { age: 30 };
// let combinedObj = { ...obj1, ...obj2 };

// console.log(combinedObj); // Output: { name: "John", age: 30 }

// Object destructuring
// let person = {
//     nickname: "John",
//     age: 30,
//     city: "New York"
// };

// let { nickname, age } = person;
// console.log(nickname); // Output: "John"
// console.log(age); // Output: 30


// Cloning objects
let obj = { name: "John", age: 30 };

// // Using spread syntax
// let clone1 = { ...obj };
// console.log(clone1)
// // Using Object.assign()
// let clone2 = Object.assign({}, obj);
// console.log(clone2)

// // Using JSON
// let clone3 = JSON.parse(JSON.stringify(obj));
// console.log(clone3)
// console.log(clone1); // Output: { name: "John", age: 30 }

// Preventing object modification
// let obj = { name: "John" };

Object.freeze(obj); // Prevents any changes to the object
obj.name = "Alice"; // Change will not take effect
console.log(obj.name); // Output: "John"

