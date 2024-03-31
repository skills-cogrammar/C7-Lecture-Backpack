// Insertion sort

// Step 1 − If it is the first element, it is already sorted. return 1;

// Step 2 − Pick next element

// Step 3 − Compare with all elements in the sorted sub-list

// Step 4 − Shift all the elements in the sorted sub-list that is greater than the value to be sorted

// Step 5 − Insert the value

// Step 6 − Repeat until list is sorted

// let lst = [5,3,2,4,7,1];

let num_items = prompt('Please enter the amount of items in the list that must be sorted:');
let lst = [];

for (let i = 0; i < num_items; i++) {
    item = prompt('Enter item to have in list:');
    lst.push(item)
}

alert(`Your list is: ${lst}`);

let key;
let j;

// Loop through the array starting from the second element
for (let i = 1; i < lst.length; i++){

    // Store the current element in a variable 'key'
    key = lst[i];

    // Initialize a variable 'j' to point to the element before the current one
    j = i - 1;

    // Move elements of 'lst[0..i-1]', that are greater than 'key', to one position ahead of their current position
    while(j >=0 && lst[j] >= key){
        lst[j + 1] = lst[j];
        j = j - 1;
    }

    // Place 'key' into its correct position in the sorted subarray
    lst[j + 1] = key;
}

alert(`Your sorted list is: ${lst}`);
