#List examples continued. 
#Sorting when some items are upper case
colour_list=["blue","Orange","lavender","cyan"]
colour_list.sort() #Does not sort correctly
#print(colour_list)
colour_list.sort(key=str.lower) #Correct sorting irrespective of case
#print(colour_list)

#Reverse current sorting 
colour_list.reverse()
#print(colour_list)

#Joining lists: 3 ways
l1 = ['a','b','c']
l2 = [1,2,3]
#print(l1+l2)

#using append
for x in l2:
    l1.append(x)

#print(l1)

#using extend
l1 = ['a','b','c']
l1.extend(l2)
#print(l1)

#Check if specific character is in the list
newlist=[]

for x in colour_list:
    if "a" in x:
        newlist.append(x)

#print(newlist)