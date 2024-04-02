#Lists
import sys
fruits = ['apple','banana','orange']
#fruits.append('grape') #to add one item at the end of the list
fruits.extend(['grape','pineapple']) #to add multiples items at the end
#print(fruits)

#Length of list
print(len(fruits))

#insert item at specific location
fruits.insert(3,'blueberry')
print('Blueberry at index 3:',fruits)

#Changing a range of items
fruits[1:3] = ['kiwi','strawberry']
print('Change index 1 and 2:',fruits)

#Adding a tuple to a list
fruits_tuple = ("cherry","granadilla")
fruits.extend(fruits_tuple)
print('Added tuple to list:',fruits)

#Check types
print('Types:',type(fruits), type(fruits_tuple))

#Removing
removed_item = fruits.pop(2)
print('Removed index 2: is',removed_item)

fruits.remove("cherry")

#Deleting index 0
#del fruits[0] #without the [0], the whole list is deleted
#print(fruits)

#Clearing the list, it will be an empty list after this
#fruits.clear()

#Sorting
#print(fruits)
fruits.sort(reverse=True) #Reverse alphabetical
print('Reverse Alphabetical:',fruits)

#Looping 
fruits1 = ['apple','banana','orange']

#Same outout for all the 3 loops below
for x in fruits1:
    print(x)

for i in range(len(fruits1)):
    print(fruits1[i])    

i = 0
while i < len(fruits1):
    print(fruits1[i])
    i = i + 1