#TypeError
try:
    add_items = 4 + "34"
except TypeError as ele:
    print(f"Error: {ele}")

#ValueError
try:    
    int("We are the world")
except ValueError as ele:
    print(f"This is a ValueError: {ele}")

#NameError
try: 
    print(sub_value)
except NameError as ele:
    print(f"Error: {ele}")

#IndexError
list1 = [1,2,3,4]
try:
    print(list1[4])
except IndexError as ele:
    print(f"Error: {ele}")

#KeyError
try:
    poke = {"p": "pikachu", "c": "charizard", "s": "slowpoke"}   
    print(poke['d'])     
except KeyError as ele:
    print(f"KeyError: {ele}")    

#FileNotFoundError
try:
    with open("lyr.txt", 'r') as file:
        content = file.readlines() 
except FileNotFoundError as ele:
    print(f"Error: {ele}")  

#IOError
      
#AttributeError
# str1 = "Mangoes"
# str1.append("for sales")


#ZeroDivisionError 12/0

#KeyboardInterrupt
# try:
#     while True:
#         print("Hello")
#         pass
# except KeyboardInterrupt:
#     print("Exterminate!")            

print("This is the end.")    