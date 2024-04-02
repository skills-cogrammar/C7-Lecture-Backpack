// Once downloaded from npm, load the library into JS
var math = require('mathjs');
// var ss = require('simple-statistics');

let heights = [168, 170, 150, 160, 182, 
                140, 175, 191, 152, 150];

// Mean
let mean = math.mean(heights);
console.log(mean);

// Median
let median = math.median(heights);
console.log(median);

// Mode
let mode = math.mode(heights);
console.log(mode);

// Variance
let variance = math.variance(heights);
console.log(variance);

// Standard Deviation
let std = math.std(heights);
console.log(std);


