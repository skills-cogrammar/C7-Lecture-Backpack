""" ****** Implementing a Class with Methods ****** """

# Creating a Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return f"{self.make} {self.model} is driving."

# Class instantiation
my_car = Car("Toyota", "Camry", 2022)

# Creating and calling methods
print(my_car.drive())  # Output: Toyota Camry is driving.

""" ****** Inheritance ****** """

# ------- Single Inheritance
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Usage
dog = Dog()
print(dog.speak())  # Output: Woof!

# ------- Multiple Inheritance example
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"{self.brand} is driving."

class Electric:         # No inheritance and no constructor: see below
    def charge(self):
        return "Charging the electric vehicle."

class HybridCar(Vehicle, Electric):
    def __init__(self, brand, fuel_type):
        # Call the constructors of both parent classes
        Vehicle.__init__(self, brand)
        Electric.__init__(self)

        self.fuel_type = fuel_type

    def drive(self):
        return f"{self.brand} {self.fuel_type} is driving."

# Creating an instance
hybrid_car = HybridCar("Toyota", "Hybrid")

# Using methods from Vehicle
print(hybrid_car.drive())  # Output: Toyota Hybrid is driving.

# Using methods from Electric
print(hybrid_car.charge())  # Output: Charging the electric vehicle.

""" ****** Preparing and accessing Controlled Attributes and Methods ****** """

# Preparing Attribute Access Control
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

# Preparing Method Access Control
    def __withdraw(self, amount):  # Private method
        self.__balance -= amount

# Accessing Controlled Attributes and Methods
account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
account.__withdraw(500)  
# Error: AttributeError: 'BankAccount' object has no attribute '__withdraw'

""" ****** Encapsulation ****** """

""" ==================================
Access Modifiers are used to specify the accessibility or visibility of a class, 
its members (methods and variables), and other entities. 
Access modifiers define the scope in which these elements can be accessed. 
They are essential for implementing encapsulation, 
one of the fundamental principles of OOP.
"""

# ================ 1. Public Variable
"""
Accessible from outside the class or module.
Part of the public interface.
"""
class MyClass:
    def __init__(self):
        self.public_variable = "Accessible Everywhere"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the public variable from outside the class
print(my_object.public_variable)

# ================ 2. Protected Variable
"""
No name mangling is applied.
Conventional indication that the variable is for internal use.
Still accessible from outside the class.
"""
class MyClass:
    def __init__(self):
        self._protected_variable = "Limited Access"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the protected variable from outside the class
print(my_object._protected_variable)

# ================ 3. Private Variable
"""
Name mangling is applied.
Accessible with a mangled name from outside the class.
Not a strict access control mechanism, more of a convention.
"""
class MyClass:
    def __init__(self):
        self.__private_variable = "Secret"

# Accessing the private variable from outside the class
my_object = MyClass()

# print(my_object.__private_variable)             # Note this code gives error
print(my_object._MyClass__private_variable)       # Name mangling must be applied

""" ==================================
Getter Methods:

Getter methods, are used to retrieve the values of private or protected attributes.
They provide read-only access to the internal state of an object.
The naming convention for a getter method is typically get_attribute(), ie. get_value
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())  # Output: 42

"""
Setter Methods:

Setter methods, are used to modify the values of private or protected attributes.
They provide a way to control the modification of internal state and 
enforce validation rules. The naming convention for a setter method is 
typically set_attribute().
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the setter method to modify the value
my_object.set_value(50)

"""
Setter & Getter combination to run.
"""
# Getter Method:
class MyClass:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value
    
    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())

# Setter Method:

# Using the setter method to modify the value
my_object.set_value(50)

# Using the getter method to access the modified value
print(my_object.get_value())

""" ****** Polymorphism in Class Design ****** """

# ------- Super() and Method Overriding """
class Animal:
    def make_sound(self):
        return "Generic animal sound"

    def move(self):
        return "Animal is moving"

class Dog(Animal):
    def make_sound(self):
        return "Woof, woof!"

    def fetch(self):
        return "Dog is fetching the ball"

    def move(self):
        # Call the parent class's move method and add additional behavior
        parent_move = super().move()
        return f"{parent_move} with a wagging tail"

class Cat(Animal):
    def make_sound(self):
        return "Meow, meow!"

    def climb_tree(self):
        return "Cat is climbing the tree"

    def move(self):
        # Call the parent class's move method and add additional behavior
        parent_move = super().move()
        return f"{parent_move} gracefully"

# Creating instances
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Using methods from Animal class
print(generic_animal.make_sound())  # Output: Generic animal sound
print(generic_animal.move())        # Output: Animal is moving

# Using overridden make_sound methods
print(dog.make_sound())             # Output: Woof, woof!
print(cat.make_sound())             # Output: Meow, meow!

# Using additional methods in subclasses
print(dog.fetch())                  # Output: Dog is fetching the ball
print(cat.climb_tree())             # Output: Cat is climbing the tree

# Using overridden move methods that utilise the parent class's method
print(dog.move())                   # Output: Animal is moving with a wagging tail
print(cat.move())                   # Output: Animal is moving gracefully

# ------- Dunder Methods

"""
A class called Person with a custom dunder method __call__.
The __call__ method allows instances of the class to be called
as if they were functions.
"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def __call__(self, other_person):
        return f"{self.name} says: Hi, {other_person.name}!"


# Creating instances of Person
alice = Person("Alice")
bob = Person("Bob")

# Using the greet method
print(alice.greet())  # Output: Hello, my name is Alice!
print(bob.greet())    # Output: Hello, my name is Bob!

# Using the __call__ method, allowing instances to be called like functions
# Below is same as calling alice.__call__(bob)
print(alice(bob))  # => Output: Alice says: Hi, Bob!
print(bob(alice))  # => Output: Bob says: Hi, Alice!

"""
If a custom class does not implement the __len__ method, calling the 
len() function on an instance of that class will result in a TypeError. 
This is because the len() function relies on the presence of the __len__ method 
to determine the length of an object.
"""
class MyCollection:
    def __init__(self, items):
        self.items = items

# Create an instance of MyCollection
my_jazz = MyCollection([1, 2, 3, 4, 5])

# Attempt to use the len() function
print(len(my_jazz))  # Raises TypeError: object of type 'MyCollection' has no len()


"""
The __len__ method is used to define the behaviour of the len() function 
when called on an instance of a class. 
By implementing the __len__ method in a class, you can control what value 
is returned by len() for instances of that class.
"""
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# Create an instance of MyCollection
my_collection = MyCollection([1, 2, 3, 4, 5])

# Use the len() function to get the length of the instance
print(len(my_collection))  # Output: 5


# ------- Operator Overloading
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return Circle(self.radius + other)
        else:
            raise TypeError("Unsupported operand types")


# Usage
c1 = Circle(5)
c2 = Circle(3)
c3 = c1 + c2
print(c3.radius)  # Output: 8

# ------- Method Overloading

""" 
Below is an example of how method overloading is supposed to work.
This is however not supported by Python since there are many alternatives.
"""
class MathOperations:
    def add(self, a, b):
        return a + b

    #Since Python does not support overloading, overwriting is applied here.
    def add(self, a, b, c):
        return a + b + c

# Create an instance of the MathOperations class
math_instance = MathOperations()

# Call the add method with different numbers of arguments
result_2_params = math_instance.add(2, 3)           # Calls the first add method
result_3_params = math_instance.add(2, 3, 4)        # Calls the second add method

print(result_2_params)  # Output: 5
print(result_3_params)  # Output: 9

# ========== Alternative to how Python can deal with above - using *args
class MathOperations:
    def add(self, *args):
        if len(args) >= 2:
            numbers = [num for num in args]
            result = sum(numbers)
            return result
        else:
            raise ValueError("Invalid number of arguments")

# Create an instance of the MathOperations class
math_instance = MathOperations()

# Call the add method with different numbers of arguments
result_2_params = math_instance.add(2, 3)          
result_3_params = math_instance.add(2, 3, 4)      

print(result_2_params)  # Output: 5
print(result_3_params)  # Output: 9

# ------- Duck Typing

""" Where the type or class of an object is less important 
    than the methods it defines or the behaviour it exhibits. """
class Bird:
    def fly(self):
        return "The bird is flying"

class Airplane:
    def fly(self):
        return "The airplane is flying"

class Helicopter:
    def fly(self):
        return "The helicopter is flying"

# Demonstrating duck typing with another class
class Superhero:
    def fly(self):
        return "The superhero is flying"

# A function that relies on duck typing
def let_it_fly(flying_object):
    # This function does not care about the type of flying_object
    # as long as it has a 'fly' method
    return flying_object.fly()

# Creating instances of Bird, Airplane, Helicopter and Superhero
sparrow = Bird()
boeing = Airplane()
chopper = Helicopter()
hero = Superhero()

# Using the let_it_fly function with different types of objects
print(let_it_fly(sparrow))   # Output: The bird is flying
print(let_it_fly(boeing))    # Output: The airplane is flying
print(let_it_fly(chopper))   # Output: The helicopter is flying
print(let_it_fly(hero))      # Output: The superhero is flying
