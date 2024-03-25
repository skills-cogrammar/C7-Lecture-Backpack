#Example 1: Division by zero

def divide(num1,num2):
    print(num1/num2)

#divide(10,0.0001) #Instead of divinding by 0, divide by a very small number

#2. Name error
name = "Luke"
#print('Hello, '+name)

#3. Syntax error
def say(name):
    print("Hello, "+nam) #Change nam to name

#say("Luke")

#4. Type error
#sum_value = str(45) + "tree" #Uncomment this to run and see the type error
#print(sum_value)

#Example 5. Typeerror or Syntax error
a=(1,20,18) #Since 'a' is a tuple, the next line (when uncommented) will give an error, tuples are immutable
#a[2] = 30 #run this after chaning 'a' to a list in the line above
#print(a)
#print(len(a))

#Example 6. Index error
#print(a[3]) #a is a list which has only 3 items, so index 0,1,2.

#Others: Attribute error, Import Error, Value Error, Key Error, Index error, IO Error

#---------------------------

#Debugging
#Uncomment to run, infinte while loop, Ctrl + C to exit
x=0
# while x < 5: # Either make this x > -5 fix by changing the logical expression
#     print(x)
#     x -= 1 #Or fix by changing the update to +=


#adds sum of numbers from 0 to n
def addsum(n):    
    total = 0
    for i in range(n): #Step 3: To sum till 5, use range(n+1)=range(6)
        #print(i) #Step 1: Add print statement for intermediate values, see that only 1st iteration is done
        total +=i
        return total #Step 2. Unindent return so that the for loop runs for the whole range, still only till 4

#Adding all number till 5, it should give 15. However, we get 0 with above function.
print(addsum(5))