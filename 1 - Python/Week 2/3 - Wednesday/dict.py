#Dictionaries
car_dict =  {
    "brand": "VW",
    "model": "Polo",
    "year":2018,
    "year":2024 #repeating key, but no duplicate keys allowed, so only last value is retained
}

#Fetch key
#print(car_dict["model"])
x = car_dict.get("model")
#print(x)

#Get keys with car_dict.keys(), values with car_dict.values(), or boths as follows
print(car_dict.items())

#To check if a specific key is present in the dict
if "model" in car_dict:
    print("Yes, 'model' is one of the keys in this dictionary.")

#Update value
car_dict.update({"year":1999})    
#print(car_dict)

#Remove a key, the value will also be removed
car_dict.pop("model")
print(car_dict)

#Remove a key using del, without the key value, whole dict can be deleted
#del car_dict["year"]
#print(car_dict)

#Copy to another dictionary with any of the 2 methods below
#car_dictionary = car_dict.copy()
#car_dictionary = dict(car_dict)

#Nested dictionaries

child1 = dict(name="Adam",age=8) #Use dict to create this dict
child2 = dict(name='Ben',age=10)
child3 = {"name":"Charlize","age":7} #Use {} to create this dict

class_list = {"child1":child1,"child2":child2,"child3":child3} #Nested dic

print(class_list)
print(class_list["child2"]["name"])