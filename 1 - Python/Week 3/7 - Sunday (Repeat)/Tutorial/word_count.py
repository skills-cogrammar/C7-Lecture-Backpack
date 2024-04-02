def count_words():
    filename = input("Enter the file name: ")
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("No file of that name.")

    else:
        count = 0
        data = file.read()
        word = data.split() #Split entire content of file into separate words
        for i in word:
            count +=1
        print("Total words are: ", count)
        file.close()

count_words()
