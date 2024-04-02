# TypeError
added_value = 4 + "phone"

# ValueError
int("the bats are flying quite low tonight")

# NameError
# access a variable that doesn't exist 
print(sub_value)

# IndexError
user_list = [12, 23, 34]
print(user_list[5])

# KeyError
poke = {"p": "pikachu", "c": "charizard", "s": "slowpoke"}
print(poke['s'])

# ZeroDivisionError
print(12/0)

# FileNotFoundError
with open("cats.txt", 'r') as file:
    content = file.readlines()

# IOError
with open("cats.pdfwordpngjpeg", 'r') as file:
    content = file.readlines()

# AttributeError
random_string = "Mangoes"
random_string.append("for sale")

# KeyBoardInterrupt
while True:
    print("hi, what doing ? ")
    pass
