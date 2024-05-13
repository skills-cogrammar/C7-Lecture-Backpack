// Task 7 Tips

let firstName = "Conscious";
let noVowels = "";
let char;

// for (let i = 0; i < firstName.length; i++){
//     char = firstName[i];
//     console.log(char);

//     if (['a', 'e', 'i', 'o', 'u'].includes(char)){
//         continue;
//     } else {
//         noVowels += char;
//     }
// }

for (let char of firstName){
    console.log(char);

    if (['a', 'e', 'i', 'o', 'u'].includes(char)){
        continue;
    } else {
        noVowels += char;
    }
}

console.log(noVowels);

let counter = 0;
let input = "Zahra";
let output = ""

while (counter < input.length){
    char  = input[counter];
    output = char + output;
    counter += 1;
}

console.log(output);


// Task 8 Tips

function calculateQuadraticEquation(a, b, c) {
    let x1, x2, num, den;
    num = Math.pow(b, 2) - (4 * a * c);

    if (num < 0) {
        console.log("ERROR: Can't calculate squareroot of negative number");
        return;
    } 

    num = Math.sqrt(num);
    den = 2 * a;
    x1 = (-b + num) / den;
    x2 = (-b - num) / den;

    return [x1, x2];
}

let coeff = [7, 9, 10, -2, -53, 19];
console.log(calculateQuadraticEquation(coeff[0], coeff[1], coeff[3]));


function shell(shellType) {
    let type = shellType;

    function slug() {
        return type;
    }

    return slug;
}

let pickUpShell = shell("Spiral");
console.log(pickUpShell());

pickUpShell = shell("Brown");
console.log(pickUpShell());


// Task 9 Tips

// myMapper(array, f): (array) -> (f(array))
// array: array of words, at least 3 longer than 10 characters
// f: cuts the word to 6 characters

function myMapper(wordArray, mapFunction){
    let newArray = [];

    for (let word of wordArray){
        newArray.push(mapFunction(word));
    }

    return newArray;
}

function cutWord(word){
    if (word.length > 6){
        return word.slice(0, 6);
    } else {
        return word;
    }
}

// Wrapper Mapper
function Mapper (mapFunction) {
    function myWordMapper(wordArray) {
        let newArray = [];

        for (let word of wordArray){
            newArray.push(mapFunction(word));
        }

        return newArray;
    }

    return myWordMapper
}


let result = myMapper(["jkahfh", "jhqgfj", "dyastyasfd", "jahdwgqwuyd"], cutWord);
result = myMapper(["adkjaf", "akjsgdkja", "weygqwuyet"], cutWord)
console.log(result);

let mapperFunction = Mapper(cutWord);
console.log(mapperFunction(["jkahfh", "jhqgfj", "dyastyasfd", "jahdwgqwuyd"]));
console.log(mapperFunction(["adkjaf", "akjsgdkja", "weygqwuyet"]));


// Doomsday Clock
function decrement() {
    console.log(counterClock)
    counterClock -= 1
}

let intervalID;
let counterClock = 100;

let startCounter = function () {
    intervalID = setInterval( 
       decrement, 500
    );
}

function endCounter() {
    clearInterval(intervalID);
}

function reverserCounter() {
    counterClock += 10;
}

let startButton = document.getElementById('start');
let endButton = document.getElementById('end');
let reverseButton = document.getElementById('reverse');

startButton.addEventListener("click", startCounter);
endButton.addEventListener("click", endCounter);
reverseButton.addEventListener("click", reverserCounter);




