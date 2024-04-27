// Create a module and initialise NPM

// This module needs to calculate the mean, mode and median of a list of marks
// [89, 92, 39, 76, 100, 56, 92, 93, 45, 58, 76, 32, 17, 76]
const math = require("mathjs");

let marks = [89, 92, 39, 76, 100, 56, 92, 93, 45, 58, 76, 32, 17, 76];
let mean = math.mean(marks);
console.log(mean);
let mode = math.mode(marks);
console.log(mode[0]);
let median = math.median(marks);
console.log(median);

// Set up script to run the code when module-run is executed
