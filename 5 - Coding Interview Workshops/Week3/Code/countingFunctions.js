// First define the factorial function
// This is a recursive function
function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// Now we can define the combination and permutation functions

// The number of ways to arrange items
function permutations(n, r) {
    return factorial(n) / factorial(n - r);
}

// The number of ways to select items
function combinations(n, r) {
    return factorial(n) / (factorial(r) * factorial(n - r));
}

// Number of combinations of 3 items from a set of 5
let numC = combinations(5, 3);
console.log(numC); // Output: 10

// Number of permutations of 3 items from a set of 5
let numP = permutations(5, 3);
console.log(numP); // Output: 60