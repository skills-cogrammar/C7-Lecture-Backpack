#Example of classes, objects, and inheritance.
class Cat:
    def __init__(self,name="Fluffy",age=6,colour="Black"): #name, age, colour are attributes
        """ Initialise a cat object. The function defines an initialization method for a class that 
        takes in a name, age, and colour as parameters.

        :param name: The `name` parameter in the `__init__` method is used to
        store the name provided by the user when creating an instance of the class. It is assigned to
        the `name` attribute of the class instance
        """
        self.name = name 
        self.age = age
        self.colour = colour

    def speak(self):
        """ The function `speak` returns a string with the name of the object. 
        The cat makes a noise
        """  
        print(f"{self.name} says Meow!")
        #return f"{self.name} says MEEEEOOOOOWW!"

    def describe(self):
        """ Prints a description of the cat
    
        """ 
        print("My name is %s, I am %d years old and have %s fur.\n" % (self.name, self.age, self.colour))

cat1 = Cat("Mrs Norris", 10, "Orange")
#Getting all the attributes: cat1.__dict__
print("The attributes of the class Cat is: ",list(cat1.__dict__))
print("The attribute values of Cat 1 are: ", list(cat1.__dict__.values()))

cat2 = Cat("Sylvester")

print(cat1.name)
print(cat1.age)
print(cat1.colour)

print(cat2.name)
print(cat2.age)
print(cat2.colour)

# cat_name = input("what is your cat name?")
# cat_age = int(input("How old is your cat?"))
# cat_colour = input("What colour is your cat? ")

# `my_unique_cat = Cat(cat_name, cat_age, cat_type)` is creating a new instance of the `Cat` class
# with the attributes provided by the user. The `cat_name`, `cat_age`, and `cat_type` values entered
# by the user are used to initialize the attributes `name`, `age`, and `type` of the `my_unique_cat`
# object, respectively. This instance represents a unique cat object with the specified
# characteristics provided by the user.
# my_unique_cat = Cat(cat_name, cat_age, cat_colour)
# print(my_unique_cat.name)
# print(f"My cat's name is {my_unique_cat.name}")
 
#Inheritance       
#-------------------------------------------------------------------------------------------------------------
class Lion(Cat):
    """Lions inherit all properties of Cats, but we can override functions, or add new ones.
    
    """
    
    def __init__(self, name):
        """Makes a lion.
        
        """
        
        self.name=name
        self.age=4
        self.colour="yellow"
        
        
    def speak(self):
        """Lions roar.
        
        """
        print("Roar!")

#-------------------------------------------------------------------------------------------------------------
mittens=Cat("Mittens")
fluffy=Cat("Fluffy", age= 3, colour = "white")
simba=Lion("Simba")
    
mittens.speak()
mittens.describe()
fluffy.speak()
fluffy.describe()
simba.speak()
simba.describe()