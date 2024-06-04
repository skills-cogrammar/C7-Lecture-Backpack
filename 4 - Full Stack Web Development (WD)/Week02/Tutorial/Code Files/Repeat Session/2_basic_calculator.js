// Exercise: Build a calculator that take in input from the user and performs 
// simple addition, subtraction or division.

// Step 1
// input_operation = prompt("Enter a sign for the operation +, - or /")

// Step 2
// Improvement


let allowed_ops = ["+", "-", "/", "*"]
let input_operation;

do {
    input_operation = prompt("Enter a sign for the operation +, - or /");
    console.log(input_operation);
}
while (!allowed_ops.includes(input_operation));

alert('To stop anytime, enter: q');
let input_number = prompt(`Operation ${input_operation} selected. Enter number to operate:` );
let total = input_number;
let first = true;

while (input_number != 'q'){
    if (first){
        total = Number(total);
        first = false;
        continue;
    }
    
    total = eval(`${total} ${input_operation} ${input_number}`);
    // eval -> converts the string to an expression, then evaluates it eval("console.log("hello")") -> console.log("hello") -> hello 
    console.log(total);
    input_number = prompt(`Operation ${input_operation} selected. Enter number to operate: ` );
}

alert(`Your operation computes to: ${total}`);
