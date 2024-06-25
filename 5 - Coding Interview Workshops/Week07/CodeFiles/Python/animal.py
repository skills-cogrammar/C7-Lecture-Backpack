class Animal:
    def __init__(self, name):
        self.name = name
    
    def sayHi (self):
        print("Hi, I am a " + self.name)

class Mammal (Animal):
    def __init__(self, name, gestationPeriod):
        super().__init__(name)
        self.gestation = gestationPeriod

mammal = Mammal("Zebra", 12)
mammal.sayHi()

