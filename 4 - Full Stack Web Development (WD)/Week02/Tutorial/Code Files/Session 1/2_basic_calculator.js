// Exercise: Build a calculator that take in input from the user and performs 
// simple addition, subtraction or division.

// Step 1
// input_operation = prompt("Enter a sign for the operation +, - or /")

// Step 2
// Improvement


let allowed_ops = ["+", "-", "/"]
let input_operation;

do {
    input_operation = prompt("Enter a sign for the operation +, - or /");
    console.log(input_operation);
}
while (!allowed_ops.includes(input_operation));


let input_number = Number(prompt(`Operation ${input_operation} selected. Enter number to operate:` ));
let combined_operation = 0;

while (input_number != -1){
    combined_operation = eval(`${combined_operation} ${input_operation} ${input_number}`);
    console.log(combined_operation);
    input_number = Number(prompt(`Operation ${input_operation} selected. Enter number to operate: ` ));
}
alert(`Your operation computes to: ${combined_operation}`);
