
def count_words():
    file_name = input("Enter the file name to check: ")
    try:
        file = open(file_name,"r")
    except FileNotFoundError:
        print("No file by that name")
    else:
        count = 0
        data = file.read()
        words = data.split()
        for _ in words:
            count += 1
        print("Total words are",count)
        file.close()

count_words()