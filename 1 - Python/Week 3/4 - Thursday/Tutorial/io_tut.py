#Exceptions: Events detected during that execution that interupts the flow of a program

# read from file
file_name = input("Enter your file name: ")
content = ""
try:
    with open(file_name, 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"The file named {file_name} does not exist :(")
print(content)



# write from file
file_name = 'written_text.txt'
sentences = ""
sentence = input("Enter your text: ")
try:
    with open(file_name, 'w') as file:
        file.write(sentence)
except FileNotFoundError as e:
    print(f"The file named {file_name} does not exist :(")

