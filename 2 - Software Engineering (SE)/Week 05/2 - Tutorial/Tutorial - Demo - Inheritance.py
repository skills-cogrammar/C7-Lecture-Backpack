# ==================== Class Inheritance demo ====================

"""=============================
Method Overriding example
"""
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

class Cat(Animal):
    def make_sound(self):
        return "Meow, meow!"

    def climb_tree(self):
        return "Cat is climbing the tree"

# Creating instances
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Using methods from Animal class
print(generic_animal.make_sound())  # Output: Generic animal sound
print(generic_animal.move())        # Output: Animal is moving

# Using inherited methods in subclasses
print(dog.move())                   # Output: Animal is moving
print(cat.move())                   # Output: Animal is moving

# Using overridden make_sound methods
print(dog.make_sound())             # Output: Woof, woof!
print(cat.make_sound())             # Output: Meow, meow!

# Using additional methods in subclasses
print(dog.fetch())                  # Output: Dog is fetching the ball
print(cat.climb_tree())             # Output: Cat is climbing the tree

"""=============================
Multiple Inheritance example
"""
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"{self.brand} is driving."

class Electric:         
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        return "Charging the electric vehicle."

class HybridCar(Vehicle, Electric):
    def __init__(self, brand, fuel_type, battery_capacity):
        # Using super() Calls 
        super().__init__(brand)  # Call the constructor of Vehicle
        # Using Direct Calls
        Electric.__init__(self, battery_capacity)  # Call constructor of Electric
        self.fuel_type = fuel_type

    def drive(self):
        return f"{self.brand} {self.fuel_type} is driving."
    
    def display_battery_capacity(self):
        return f"The battery capacity of {self.brand} is {self.battery_capacity} kWh."

# Creating an instance
hybrid_car = HybridCar("Toyota", "Hybrid", battery_capacity = 100)

# Using methods from Vehicle
print(hybrid_car.drive())   # Output: Toyota Hybrid is driving.

# Using methods from Electric
print(hybrid_car.charge())  # Output: Charging the electric vehicle.

# Using method to display battery capacity
print(hybrid_car.display_battery_capacity())  
    # Output: The battery capacity of Toyota is 100 kWh.

# ================
# Note for the above that classes can exist without a constructor.
"""
If Electric class doesn't have a constructor, it will not explicitly inherit 
from any other class, but it implicitly inherits from the object class. 
Therefore, Electric will inherit the default constructor (__init__) 
from the base object class, even though it's not explicitly mentioned.
An illustration of the default constructor is:
-----------------
class object:
    def __init__(self):
        pass
-----------------
implemented in C as part of the Python runtime.
"""
# ==================== Special Methods demo ====================

# =============== Rectangle class with special methods 
"""
Instantiation: __init__
Custom Method: get_area
Operator Overloading: __add__, and __sub__
Comparator: __gt__, and __ge__
Representation: __str__, and __repr__
""" 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
    def __add__(self, other):
        # Custom addition operation for rectangles
        length = self.length + other.length
        width = self.width + other.width
        return Rectangle(length, width)
    
    def __sub__(self, other):
        # Custom subtraction operation for rectangles
        length = self.length - other.length
        width = self.width - other.width
        return Rectangle(length, width)
    
    def __gt__(self, other):
        # Greater than comparison based on area
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        # Greater than or equal to comparison based on area
        return self.get_area() >= other.get_area()
    
    def __str__(self):
        # String representation for print() and str()
        return f"Rectangle with length={self.length} and width={self.width}"
    
    def __repr__(self):
        # String representation for repr()
        return f"Rectangle(length={self.length}, width={self.width})"

# Creating instances of Rectangle and performing addition
rect1 = Rectangle(11, 6)
rect2 = Rectangle(7, 3)
rect3 = rect1 - rect2  # Uses the __sub__ method

# Using comparison operators (__gt__ and __ge__)
print("Comparison using __gt__:")
print(f"Is rect1 > rect2? {rect1 > rect2}")  
    # Output: True (Area of rect1 > area of rect2)

print("\nComparison using __ge__:")
print(f"Is rect1 >= rect2? {rect1 >= rect2}")  
    # Output: True (Area of rect1 >= area of rect2)

# Using __str__ and __repr__ methods
print(rect3)        # Output: Rectangle with length=5 and width=10
print(str(rect3))   # Output: Rectangle with length=5 and width=10
print(repr(rect3))  # Output: Rectangle(length=4, width=3)

# Accessing the area using get_area() method
print(rect3.get_area())  # Output: 12
    
# =============== ContactList class with special methods 
"""
Instantiation: __init__
Addressing Container-Like Objects: __getitem__, __len__, and __contains__
""" 
class ContactList:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def __getitem__(self, key):
        # Custom method to retrieve items by index
        return self.contact_list[key]
    
    def __len__(self):
        # Custom method to get the length of the contact list
        return len(self.contact_list)
    
    def __contains__(self, item):
        # Custom method to check if a contact is in the list
        for contact in self.contact_list:
            if contact.name == item:
                return True
        return False
    
    def __iter__(self):
        # Make the ContactList object iterable
        self.index = 0
        return self
    
    def __next__(self):
        # Implement next() to iterate over contacts
        if self.index < len(self.contact_list):
            contact = self.contact_list[self.index]
            self.index += 1
            return contact
        else:
            raise StopIteration
            # print("Iteration finished.")

class Contact:
    def __init__(self, name):
        self.name = name 
		
    def __str__(self):
        return f"Contact: {self.name}"

# Creating instances of ContactList and Contact, and performing operations
contact_list = ContactList()

# Utilising the custom method add_contact
contact_list.add_contact(Contact("James"))
contact_list.add_contact(Contact("Joe"))

# Utilising the special method __getitem__
print(contact_list[1])

# Utilising the special method __contains__
if "James" in contact_list:
    print("James is here.")

# Utilising special methods __iter__, __next__ and __len__
# Iterating over ContactList using for loop
print("Iterating over ContactList:")
for contact in contact_list:
    print(contact)

# Code to bring clarity to what is happening in for-loop
print("\n===== Using iter and next separately\n")
# Using the iterator
my_contact = iter(contact_list)

# Iterating using next()
if contact_list.index <= len(contact_list):
    print(next(my_contact))  # Output: James

if contact_list.index <= len(contact_list):
    print(next(my_contact))  # Output: Joe

# Attempting to go beyond the end of the iteration
if contact_list.index < len(contact_list):
    print(next(my_contact))  # Not executed

#===========================  BONUS: BATS  ===========================
"""
Using super() function for double inheritance of subclasses
"""
class Animal:
    def __init__(self, species: str = "") -> None:
        self.species = species

    def make_sound(self):
        return f"The {self.species} makes a generic sound."

class Mammal(Animal):
    def __init__(self, fur_colour: str, species: str = "Mammal") -> None:
        super().__init__(species)  
        self.fur_colour = fur_colour
        
    def show_colour(self):
        return f"The {self.species} is a {self.fur_colour} colour."
    
    def give_birth(self):
        return f"The {self.species} gives birth to live young."

class Bird(Animal):
    def __init__(self, beak_type: str, species: str = "Bird") -> None:
        super().__init__(species)
        self.beak_type = beak_type
    
    def fly(self):
        return f"The {self.species} is flying with its {self.beak_type} beak."

class Amphibian(Animal):
    def __init__(self, skin_type: str, species: str = "Amphibian", ) -> None:
        super().__init__(species)

        self.skin_type = skin_type

    def jump(self):
        return f"The {self.species} jumps with it's {self.skin_type} skin."
    
class Bat(Mammal, Bird):
    def __init__(self, fur_colour: str, beak_type: str, species: str = "Bat") -> None:
        # Use super() to call constructors of parent classes
        Mammal.__init__(self, fur_colour, species)
        Bird.__init__(self, beak_type, species)

    def echolocate(self):
        return f"The {self.species} is using echolocation."

# ============ Main Code
# Create instances
mammal_instance = Mammal("golden", "Lion")
bird_instance = Bird("hooked", "Eagle")
amphibian_instance = Amphibian("smooth", "Frog")
bat_instance = Bat("brown", "sharp", "Bat")

# Display information about animals
print(mammal_instance.make_sound())
print(mammal_instance.show_colour())
print(mammal_instance.give_birth())
print("===============")

print(bird_instance.make_sound())
print(bird_instance.fly())
print("===============")

print(amphibian_instance.make_sound())
print(amphibian_instance.jump())
print("===============")

print(bat_instance.make_sound())
print(bat_instance.echolocate())
print("===============")
