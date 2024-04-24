#Encapsulation
"""
Public access: Public variable can be accessed by any part
colour variable and start method can be accessed by any part
"""
class Car:
    color = "red"

    def start(self):
        print("Car started!")

"""
Private variables and methods can only be accessed within the class
written with double underscores (__)
Protected access: Can be accessed by the class and subclasses
written with single underscore (_)
"""        
class Car:
    __engine_capacity = 2000 #private
    _mileage = 0 #protected

    def __start_engine(self):
        self._mileage += 10
        print("Engine started")

#Example 1:
class Person:
    _name = "John" #private variable, change to protected

    def _greet(self): #private method, change to protected
        print("Hello, my name is ", self._name)

#Create an instance of the class Person
p1 = Person()
# p1._name
# p1._greet()

#Polymorphism & Inheritance
class Bird:
    def intro(self):
        print("There are many species of birds.")

    def flight(self):
        print("Most birds can fly but some cannot.")

#Inheritance
class robin(Bird):
    def flight(self):
        print("Robins can fly!")        

class ostrich(Bird):
    pass
    # def flight(self):
    #     print("Ostriches cannot fly")

bird = Bird()
bird_robin = robin()
bird_ostrich = ostrich()

bird.intro()
bird.flight()

bird_robin.intro()
bird_robin.flight()

bird_ostrich.intro()
bird_ostrich.flight()

#Abstraction
from abc import ABC #abstractmethod

class Car(ABC):
    def mileage(self):
        pass
    

