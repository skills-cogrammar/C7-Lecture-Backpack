#Python examples used in lecture

#Binary to decimal
b = "11001"
#print("Binary " + b + " to decimal:", int(b,2))
#Output: Binary 11001 to decimal: 25

#Decimal to Binary
decNum  = 26076
#decNum = int(input("Enter any Decimal Number: "))

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 

print('Decimal ' + str(decNum) + ' to binary:', decimalToBinary(decNum))
#Output: Decimal 123 to binary: 1111011

#Octal to Decimal
n = "1071"
def OctToDec(n): 
    return int(n, 8)
  
#print("Octal " + n + " to decimal:",OctToDec(n))
#Output: Octal 1071 to decimal: 569

#Decimal to Octal
def decToOct(n):
    return oct(n).replace("0o", "")
     
num = 330
#print("Decimal " + str(num) + " to octal:", decToOct(num))
#Output: Decimal 330 to octal: 512

#Hexadecimal to Decimal
hex_num = "2B4"
def hexToDec(n): 
    return int(n, 16)
  
print("Hexadecimal " + hex_num + " to decimal:", hexToDec(hex_num))
#Output: Hexadecimal 2B4 to decimal: 692

#Decimal to Hexadecimal

def decToHex(n):
    return hex(n).replace("0x", "")

num = 798

print("Decimal " + str(num) + " to hexadecimal:", decToHex(num))
#Output: Decimal 798 to hexadecimal: 31E


#Factorial 
num = 5
fact = 1
for i in range(1, num+1):
    fact = fact * i
 
print("The factorial of "+str(num)+" is: ", fact)
#Output: The factorial of 5 is:  120

#Using math
import math
print("The factorial of "+str(num)+" is: ", math.factorial(num))
#Output: The factorial of 5 is:  120


# Python program to show bitwise operators
a = 10
b = 4

print("a = ", a, '(decimal)', bin(a), '(binary)') 
print("b = ", b, '(decimal)', bin(b), '(binary)') 

# Print bitwise AND operation
print("AND: a & b =", a & b, '(decimal)', bin(a & b), '(binary)')
 
# Print bitwise OR operation
print("OR: a | b =", a | b, '(decimal)', bin(a | b), '(binary)')
 
# Print bitwise NOT operation
print("NOT: ~a =", ~a, '(decimal)', bin(~a), '(binary)')
 
# Print bitwise XOR operation
print("XOR: a ^ b =", a ^ b, '(decimal)', bin(a ^ b), '(binary)')

# Print bitwise left shift operation
print("Left shift: a << 1 = ", a << 1, '(decimal)', bin(a << 1), '(binary)')

# Print bitwise right shift operation
print("Left shift: a >> 1 = ", a >> 1, '(decimal)', bin(a >> 1), '(binary)')


def function(n, k):
    bit = n & (1 << k)
    return print(bool(bit))

function(5,2)

#XOR to flip two numbers
a=10
b=20
a=a^b
print(bin(a))
b=a^b
print(bin(b))
a=a^b
print(bin(a))
print(a,b)