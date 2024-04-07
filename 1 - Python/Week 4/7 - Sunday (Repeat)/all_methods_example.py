class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #A class method to created a Person object's age by birth year
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name, 2024 - year)
    
    #A static method to check if a Person object is an adult or child
    @staticmethod
    def isAdult(age):
        if age >= 18:
            print("This person is an adult.")
        else:
            print("This person is a child.")            
    
#Make a Person instance
person1 = Person("Bluey",7)
#Using the classmethod
person2 = Person.fromBirthYear("Bingo",2019)

print(person1.age)
print(person2.age)

#Use the staticmethod
Person.isAdult(42)