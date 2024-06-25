//JavaScript examples used in lecture

let bnum = "11001";
//onsole.log("Binary " + b + " to decimal:", parseInt(b, 2));
//Output: Binary 11001 to decimal: 25


let decNum = 123
function decimalToBinary(n) {
    return (n >>> 0).toString(2);
}
//console.log('Decimal '+ decNum + ' to binary:', decimalToBinary(decNum));
//Output: Decimal 123 to binary: 1111011

const n = "1071";
function OctToDec(n) {
    return parseInt(n, 8);
}
//console.log("Octal " + n + " to decimal:", OctToDec(n));
//Output: Octal 1071 to decimal: 569

function decToOct(n) {
    return (n).toString(8);
}
var num_oct = 330;
//console.log("Decimal " + num_oct + " to octal:", decToOct(num_oct));
//Output: Decimal 330 to octal: 512

const hex_num = "2B4";
function hexToDec(n) {
    return parseInt(n, 16);
}
//console.log("Hexadecimal " + hex_num + " to decimal:", hexToDec(hex_num));
//Output: Hexadecimal 2B4 to decimal: 692

function decToHex(n) {
    return n.toString(16);
}

var num_dec = 798;
console.log("Decimal " + num_dec + " to hexadecimal:", decToHex(num_dec));
//Output: Decimal 798 to hexadecimal: 31E



//Logic gates

//NOT gate
function NOT(a) {
    return !a;
}
console.log('NOT(1):', NOT(1));
console.log('NOT(0):',NOT(0));
//Output: false, true

//AND gate
function AND(a, b) {
    if (a === 1 && b === 1) {
        return true;
    } else {
        return false;
    }
}
console.log('1 AND 0:',AND(1, 0));
console.log('1 AND 1:',AND(1, 1));
//Output: false, true


//OR gate
function OR(a, b) {
    if (a === 1 || b === 1) {
        return true;
    } else {
        return false;
    }
}
console.log('0 OR 0:',OR(0, 0));
console.log('0 OR 1:',OR(0, 1));
//Output: false, true

//XOR gate
function XOR(a, b) {
    if (a !== b) {
        return true;
    } else {
        return false;
    }
}
console.log('1 XOR 1:',XOR(1, 1));
console.log('1 XOR 0:',XOR(1, 0));
//Output: false, true


let num = 5;
let fact = 1;
for (let i = 1; i <= num; i++) {
    fact = fact * i;
}
console.log("The factorial of " + num + " is: ", fact);
//Output: The factorial of 5 is: 120

//Bitwise operators

let a = 10;
let b = 4;

console.log("a = ", a, '(decimal)', a.toString(2), '(binary)');
console.log("b = ", b, '(decimal)', b.toString(2), '(binary)');

// Print bitwise AND operation
console.log("AND: a & b =", a & b, '(decimal)', (a & b).toString(2), '(binary)');

//Print bitwise OR operation
console.log("OR: a | b =", a | b, '(decimal)', (a | b).toString(2), '(binary)');

//Print bitwise NOT operation
console.log("NOT: ~a =", ~a, '(decimal)', (~a).toString(2), '(binary)');

// Print bitwise XOR operation
console.log("XOR: a ^ b =", a ^ b, '(decimal)', (a ^ b).toString(2), '(binary)');

// Print bitwise left shift operation
console.log("Left shift: a << 1 = ", a << 1, '(decimal)', (a << 1).toString(2), '(binary)');

// Print bitwise right shift operation
console.log("Left shift: a >> 1 = ", a >> 1, '(decimal)', (a >> 1).toString(2), '(binary)');



