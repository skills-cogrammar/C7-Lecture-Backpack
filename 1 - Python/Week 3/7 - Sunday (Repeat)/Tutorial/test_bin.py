#Creating binary data
prime_numbers = [2,3,5,7]
#convert list to binary data using bytearray
binary_data = bytearray(prime_numbers)

print('Binary data:',binary_data)

#Write this binary data in a file
filename = "test.bin"
with open(filename,"wb") as file:
    file.write(binary_data)

#Reading a binary file, explicit
f = open(r"C:\Users\moumi\Desktop\C7_lecture_codes\w3\tutorial\test.bin", "rb") 
#Read file data with read()
data = f.read()
#Check what is the type of data
print(type(data))

#Print byte sequence data
print(data)

#Close the file 
f.close()
