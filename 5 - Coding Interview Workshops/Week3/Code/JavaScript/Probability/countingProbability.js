var math = require('mathjs');

// Probability of a specific combination
let comboProb = 1/(math.combinations(10, 3));
console.log(comboProb);

// Probabiity of a specific permutation
let permProb = 1/(math.permutations(10, 3));
console.log(permProb);

