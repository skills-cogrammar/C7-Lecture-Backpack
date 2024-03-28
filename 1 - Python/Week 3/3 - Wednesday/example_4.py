# TypeError - incorrect datatype mixture
try:
    added_value = 4 + "phone"
except TypeError as e:
    print(f"Error: {e}")


# ValueError
try:
    int("the bats are flying quite low tonight")
except ValueError as e:
    print(f"Error: {e}")

# NameError
# access a variable that doesn't exist
try:    
    print(sub_value)
except NameError as e:
    print(f"Error: {e}")

# IndexError
try:
    user_list = [12, 23, 34]
    print(user_list[5])
except IndexError as e:
    print(f"Error: {e}")

# KeyError
try:
    poke = {"p": "pikachu", "c": "charizard", "s": "slowpoke"}
    print(poke['s'])
except KeyError as e:
    print(f"Error: {e}")


# ZeroDivisionError
try:
    print(12/0)
except ZeroDivisionError as e:
    print(f"Error: {e}")


# FileNotFoundError
try:
    with open("cats.txt", 'r') as file:
        content = file.readlines()
except FileNotFoundError as e:
    print(f"Error: {e}")


# IOError - when an input or output operation fails
try:
    with open("cats.pdfwordpngjpeg", 'r') as file:
        content = file.readlines()
except IOError as e:
    print(f"Error: {e}")


# AttributeError
try:
    random_string = "Mangoes"
    random_string.append("for sale")
except AttributeError as e:
    print(f"Error: {e}")

# KeyBoardInterrupt
try:
    while True:
        print("hi, what doing ? ")
        pass
except KeyboardInterrupt:
    print("we have terminated your leader")
