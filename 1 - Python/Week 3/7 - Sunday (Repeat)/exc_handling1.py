#try, except, else, finally
#x = 2
try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    #except:    
    print("Nothing went wrong.")    
finally:
    print("The 'try except' block is completed.")

#Raise an error
y = -1

# if y < 0:
#     raise Exception("Sorry Moumita, no numbers below zero")

z = 1.2

# if not isinstance(z, int):
#     raise TypeError("Only integers are allowed Yoda")

print('This is the end.')