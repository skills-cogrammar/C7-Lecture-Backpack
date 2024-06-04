# Modify this one
from animal import Animal
from cat import Cat

class Dog(Animal):
    def __init__(self, name, age):
        super(Dogs, self).__init__(name, age)
        self.cat_instance = Cat("", 0)

    def make_sound(self):
        print(f"{self.name} says wooo")
    
    def sleep(self):
        return self.cat_instance.sleep()