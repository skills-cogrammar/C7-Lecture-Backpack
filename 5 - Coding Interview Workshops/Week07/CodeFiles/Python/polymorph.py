# Create an interface by not defining all the methods 
class Vehicle:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def letsDrive (self):
        pass

class Motorbike (Vehicle):
    def letsDrive (self):
        print("Zooom zooom")

class Car (Vehicle):
    def letsDrive (self):
        print("Vroom vrooooom")

class Truck (Vehicle):
    def letsDrive (self):
        print("Brruuum brrruuuum")

motorbike = Motorbike("Yamaha", "Road Star", 2004)
car = Car("Volkswagen", "Polo", 2006)
truck = Truck("Ford", "F-150", 2021)

vehicles = [motorbike, car, truck]

for vehicle in vehicles:
    vehicle.letsDrive()

    