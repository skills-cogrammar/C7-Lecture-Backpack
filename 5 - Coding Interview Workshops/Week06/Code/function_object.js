// Passing function to a variable
function greet(text){
    return text.toUpperCase();
}

console.log(greet('Hello'));
let intro = greet;
console.log(intro('Hello World!'));
//Output: HELLO
//HELLO WORLD!


// Passing functions as arguments to other functions
function shout(text) {
    return text.toUpperCase();
}

function whisper(text) {
    return text.toLowerCase();
}

function greeting(helloMessage, name) {
    console.log(helloMessage("Function passed as argument in ") + name);
}

greeting(shout, "JavaScript");
greeting(whisper, "JavaScript");
//Output: FUNCTION PASSED AS ARGUMENT IN JavaScript
// function passed as argument in JavaScript
                                                                                    

// Functions returning another function
function add_sub(a, b) {
    let add = a + b;
    let sub = a - b;
    function mult(c) {
        console.log(add * sub * c);
    }
    return mult;
}

// form a object of first method
let returned_function = add_sub(5, 2);
// a=5 & b=2 -> add=7 & sub=3

// check object
console.log(returned_function);
// Output: It will be a function

// call second method by first method
returned_function(10);
// Output: 210 (With c = 10, a*b*c = 210)

// Local Scope
function myfunc() {
    let x = "Hello!";
    console.log(x);
  }
  
//myfunc();
// Output: Hello!

// Nested function
function myfunc() {
    let x = "Hello";
    function myinnerfunc() {
      console.log(x + " World!");
    }
//    myinnerfunc();
  }
  
// myfunc();
// Output: Hello World!

// Scope rules
function scopeTest() {
    function doLocal() {
        let text = "local text";
    }

    function doNonlocal() {
        text = "nonlocal text";
    }

    function doGlobal() {
        global.text = "global text";
    }

    let text = "sample text";
    doLocal();
    console.log("After local assignment:", text);
    doNonlocal();
    console.log("After nonlocal assignment:", text);
    doGlobal();
    console.log("After global assignment:", text);
}

scopeTest();
console.log("In global scope:", global.text);
// Output:
// After local assignment: sample text
// After nonlocal assignment: nonlocal text
// After global assignment: nonlocal text
// In global scope: global text

  
// Closure
function make_multiplier_of(n) {
    return function multiplier(x) {
      return x * n;
    };
  }
  
// Multiplier of 2
const times2 = make_multiplier_of(2);
  
// Multiplier of 5
const times5 = make_multiplier_of(5);
  
// times2 and times5 are closure functions
  
console.log(times2(7));
// Output: 14
  
console.log(times5(9));
// Output: 45
  
console.log(times5(times2(3)));
// Output: 30


// Pass by value
let a = 10;
let b = a;
  
a = 20;
  
console.log(a); // Outputs: 20
console.log(b); // Outputs: 10    


// Pass by reference
let obj1 = { value: 10 };
let obj2 = obj1;

obj1.value = 20;

console.log(obj1.value); // Outputs: 20
console.log(obj2.value); // Outputs: 20