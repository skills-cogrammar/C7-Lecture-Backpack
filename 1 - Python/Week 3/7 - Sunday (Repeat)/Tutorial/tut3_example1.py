# modes, r, w, a, +, x

#f = open("lyrics.txt","x")

# x - create a new file, if and only if it does not exist
# w - create a new file whether or not there is a file with the same one

#Read + write, Read + append
#r+ opens file for both reading and writing, if file does not exist, an error
#w+ opens file for reading and writing, text is overwritten

filename = 'lyrics.txt'
output = "\nWhat a wonderful world"
# with open(filename, "r+") as f:
#     data = f.read()
#     print(data)
#     #Add more content in the begining of the file
#     f.seek(0)
#     f.write(output)
#     f.truncate()

#a+ appending to the original file
with open(filename, "a+") as f:
    data = f.read()        
    print(data)
    f.write(output)