#1st func
def divide(a,b):
    return a/b

#2nd func
def func_value():
    result = divide(10,0) #Use any small number, say 0.1 instead
    print(result)

func_value() 

#Random user defined function
def string_build(word1, word2, word3, word4):
    return f"{word1}-{word2}-{word3}{word4}"

random_text = string_build("Python version",3.14, "is gr",str(8))
print(random_text)

print(type(str(8)))
