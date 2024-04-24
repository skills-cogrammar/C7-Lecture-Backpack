# Class - a blueprint for creating objects, each class knows two things about itself; Attributes and Methods
# instance / object - this here is the instance or object created from the class

# The `Cat` class defines attributes and a method for a cat object.
class Cat:
    def __init__(self, user_given_name, user_given_age, user_given_type):
        """
        The function defines an initialization method for a class that takes in a name, age, and type as
        parameters.
        
        :param user_given_name: The `user_given_name` parameter in the `__init__` method is used to
        store the name provided by the user when creating an instance of the class. It is assigned to
        the `name` attribute of the class instance

        :param user_given_age: The `user_given_age` parameter in the `__init__` method is used to store
        the age provided by the user when creating an instance of the class. It is assigned to the `age`
        attribute of the class instance
        
        :param user_given_type: This parameter is used to store the type of the cat, such as
        "persian", "orange", "norweigen forrest", etc. It allows you to categorize cats based on different breed or
        characteristics
        """
        self.name = user_given_name
        self.age = user_given_age
        self.type = user_given_type

    def speak(self):
        """
        The function `speak` returns a string with the name of the object followed by "says
        MEEEEOOOOOWW!".
        :return: The `speak` method is returning a string that includes the name of the object followed
        by "says MEEEEOOOOOWW!".
        """
        return f"{self.name} says MEEEEOOOOOWW!"
    

# an object is an instantiation of a class
# The code snippet you provided is creating instances of the `Cat` class with different attributes for
# each cat.
cat_one = Cat("Bartholomeow", 360, "orange-cat")
cat_two = Cat("Garfield", 78, "orange-cat")
cat_three = Cat("Beerus", 600, "Egyptian-kush cat")
cat_four = Cat("Meowth", 23, "Persian") 

# print(cat_one.name) 
# print(cat_three.speak())
# print(cat_one.speak())
# print(cat_two.speak())
# print(cat_four.speak())

# make user create cat object
# The code snippet `cat_name = input("what is your cat name ?")`, `cat_age = int(input("How old is
# your cat ?"))`, and `cat_type = input("Enter cat breed ? ")` is prompting the user to input
# information about their cat.
cat_name = input("what is your cat name ?")
cat_age = int(input("How old is your cat ?"))
cat_type = input("Enter cat breed ? ")

# `my_unique_cat = Cat(cat_name, cat_age, cat_type)` is creating a new instance of the `Cat` class
# with the attributes provided by the user. The `cat_name`, `cat_age`, and `cat_type` values entered
# by the user are used to initialize the attributes `name`, `age`, and `type` of the `my_unique_cat`
# object, respectively. This instance represents a unique cat object with the specified
# characteristics provided by the user.
my_unique_cat = Cat(cat_name, cat_age, cat_type)

# accessing attribute
# `print(my_unique_cat.name)` is accessing and printing the value of the `name` attribute of the
# `my_unique_cat` object. This line of code retrieves the name of the cat that the user provided when
# creating the `my_unique_cat` instance and displays it as output.
print(my_unique_cat.name)


# The line `print(f"My cat's name is {my_unique_cat.name}")` is using an f-string to format and print
# a message that includes the name of the cat stored in the `name` attribute of the `my_unique_cat`
# object.
print(f"My cat's name is {my_unique_cat.name}")


# The line `print(f"When my cat is hungry, I hear her say {my_unique_cat.speak()}")` is utilizing an
# f-string to create a formatted string.
print(f"When my cat is hungry, I hear her say {my_unique_cat.speak()}")



"""
class car:
    wheels = 4

    def __init__(self, make, model, type, color)
        self.make = make
        self.model = model
        self.type = type
        self.color = color
    
    def speed(self):
        return f"{self.make} goes at .... "
    

"""


# This is a function
# def add():
#     pass

# class math:
    #This is a function within the context of a class commonly reffered to as a method
    # def add():
    #     pass


# It came up with <bound method Cat.speak() of <__main__.Cat object at 0x108fe2270>>
