#In built functions
# print("Hello world!")

random_text = 'The quick brown fox jumps over the lazy dog.'
# print("The sentence has " + str(len(random_text)) + " characters.")

#Example 2, add numbers in a list
num_list = [12,13,14]

##1st try: For loop
total = 0
# for i in num_list:
#     #total = total + i
#     total += i
#     print(f"Current total is: {total}")

##2nd: Using sum 
# print(sum(num_list))

#Example 3: Function with arguments as input 
def add(num1,num2):
    return num1+num2

# num1_prompt = int(input("Enter 1st no. "))
# num2_prompt = int(input("Enter 2nd no. "))

# new_sum = add(num1_prompt,num2_prompt)
# print(new_sum)

#Example 4a: Order of parameters
def school_names(child3, child2, child1):
    print("The youngest child is "+ child3)

# school_names(child1='Ayanda',child2='Bongi',child3='Charlize')

#Example 4b: No of arguments unknown
def school_names(*kids):
    print("The youngest child is "+ kids[2] + ".")

# school_names("Ayanda","Bongi","Charlize")

#  If else condition in functions
def sign(num):
    if num<0:
        print("Negative number")
    elif num>0:
        print("Positive number")
    else:
        print("The number is 0.")

#sign(10)
#sign(-533)    
#sign(10/2-5) 




