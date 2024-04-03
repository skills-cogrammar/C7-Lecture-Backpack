# Convert fractional decimal to binary number, upto k-precision after decimal point  
def decimalToBinary(num, k_prec) : 
  
    binary = ""  
  
    # Get the integral part of the decimal number  
    integral = int(num)  
  
    # Get the fractional part 
    fractional = num - integral 
  
    # Conversion of integral part to binary equivalent  
    while (integral) : 
          
        rem = integral % 2
  
        # Append 0 in binary  
        binary += str(rem);  
  
        integral //= 2
      
    # Reverse string to get original binary equivalent  
    binary = binary[ : : -1]  
  
    # Append point before conversion  of fractional part  
    binary += '.'
  
    # Conversion of fractional part to binary equivalent  
    while (k_prec) : 
          
        # Find next bit in fraction  
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) : 
              
            fractional -= fract_bit  
            binary += '1'
              
        else : 
            binary += '0'
  
        k_prec -= 1
  
    return binary  

      
n = 3.14
k = 3
print(decimalToBinary(n, k)) 
  
n = 9.81
k = 5
print(decimalToBinary(n, k))