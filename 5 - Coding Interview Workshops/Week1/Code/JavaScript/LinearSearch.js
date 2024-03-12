// JavaScript Code
function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i;  // Return the index if the target is found
        }
    }
    return -1;  // Return -1 if the target is not found
}

// Example usage
const arr = [4, 2, 8, 5, 1, 9, 3];
const target = 1;
const result = linearSearch(arr, target);
if (result !== -1) {
    console.log(`Element found at index ${result}`);
} else {
    console.log("Element not found");
}