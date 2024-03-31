filename = input("Enter filename: ")
content= ""

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError as ele:
    print(f"File {filename} does not exist: ")

print(content)  

#Write to file
output_file = "written_text.txt"
#sentences = ""
sentence = input("Enter your text: ")

try:
    with open(output_file, 'w') as file:
        file.write(sentence)
except FileNotFoundError:
    print(f"The file {output_file} does not exist.")


