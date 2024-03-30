#Explicit method, relative path
file = open("list_of_jedis.txt",'r')

#Absolute path: python doesn't recognize backslash \
#Try using / instead, or with r in front 
#by converting the normal string to a raw string for the path
#Shouldn't be a problem in Mac/Linux

#file = open("C:/Users/moumi/Desktop/C7_lecture_codes/w3/lecture1/list_of_jedis.txt",'r')
#file = open(r"C:\Users\moumi\Desktop\C7_lecture_codes\w3\lecture1\list_of_jedis.txt",'r')

#Close the file
file.close()

#Implcit method, read contents of the file
with open('list_of_jedis.txt','r') as file:
    file_content = file.readlines()
    print('\nThis is the readlines() output, as a string list',file_content)
    print('File content in separate lines')
    for i in file_content:
        print(i)
    
    #Reading specific lines
    first_line = file_content[0]
    print(f"The first line is: {first_line}")

    #Setting the file's current position at the offset
    file.seek(0)

    #Read content
    content = file.read()
    print(f"\nThis is the read output: {content}")

    file.seek(0)
    
    #Readline
    content = file.readline()           
    print(f"\nThis is the readline() output: ")
    print(content)

    #Return only first two bytes from the line
    print(file.readline(2))

#Write to a file

with open("jedi.txt",'w') as file:
    user_jedi = input("What is your bad jedi name? ")
    file.write(f"\n{user_jedi}")

    good_list = ["Luke","Rey","Obi-Wan"]
    bad_list = ["Anakin","Dooku"]
    #file.writelines(good_list)

    for no_line in bad_list:
        file.write(f"\n{no_line}")

#File handling
file = open('jedi.txt','r')   #Text (t), bin (b)
# print(file.readline())

# for x in file:
#     print(x)

#Appending mode

#f = open('jedi.txt','a')
#f.write('\nNow the file has more content.')
#f.close()

f = open('jedi.txt','r')
# print(f.read())

#To create a new file, will give error if the file already exists
#f = open('filename.txt','x')

import os
#os.remove('filename.txt')

#Check if a file exist, then delete it
if os.path.exists('filename.txt'):
    os.remove('filename.txt')
else:
    print('The file does not exist')    

#Overwrite the content
#f = open('jedi.txt','w')
#f.write('Oops, I have deleted the content.')    
#f.close()