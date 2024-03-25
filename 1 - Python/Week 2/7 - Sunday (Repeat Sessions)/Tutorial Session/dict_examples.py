#Two ways to construct dictionaries
car_dict = {
    "brand": "VW",
    "model": "Polo",
    "year": 2018,
    "year": 2024
}
#print(car_dict)

car_dict1 = dict(brand="VW",model="Polo",year=2018)
#print(car_dict1)

#Get keys with car_dict.keys(), values with car_dict.values(), or boths as follows
print(car_dict.items())
#In separate lines
for x in car_dict.items(): #keys(), values()
    print(x)

#Add new items or change existing 
x = car_dict.keys()
#print(x)
car_dict["colour"] = "red"
#print(x)
#print(car_dict)

y = car_dict.values()
#print(y)
car_dict["model"] = 'Golf'
#print(y)

#To check if a key is present
if "model" in car_dict:
    print("Yes, 'model' is one of the keys in this dictionary.")

#Removing items
#print(car_dict)    
car_dict.pop("colour") #popitem #del car_dict, clear
#print(car_dict)

#Nested dictionaries
car_dict2 = dict(brand="Hyundai",model="i30", year=2020)
car_dict3 = {"brand":"Honda","model":"Civic","year":2019}

car_list = {"car1":car_dict, "car2":car_dict2, "car3":car_dict3}

#print(car_list)

##Get only car2 details, get only the brand of car2
#print(car_list["car2"]["brand"])