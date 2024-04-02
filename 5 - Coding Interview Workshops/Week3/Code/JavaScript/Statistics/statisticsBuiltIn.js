let data = [1, 2, 3, 4, 5];

// We can define some functions from scratch 
// reduce allows us to sum up the array
let sum = data.reduce((a, b) => a + b, 0);
let mean = sum / data.length;
console.log(mean); // Output: 3

let squaredDifferences = data.map(x => Math.pow(x - mean, 2));
let variance = squaredDifferences.reduce((a, b) => a + b, 0) / data.length;
let standardDeviation = Math.sqrt(variance);
console.log(standardDeviation); // Output: 1.4142135623730951