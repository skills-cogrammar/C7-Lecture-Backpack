# Create Animal base class with attributes representing and animal
class Animal:
    def __init__(self, sound: str) -> None:
        self.sound = sound

    def make_sound(self) -> str:
        return f"The {type(self).__name__} goes {self.sound}"

# Create subclasses to inherit attributes and properties from Animal
class Lion(Animal):
    pass

class Canary(Animal):
    pass

class Goldfish(Animal):
    pass

lion = Lion("rawr")
bird = Canary("tweet")
fish = Goldfish("blub")

print(lion.make_sound())
print(bird.make_sound())
print(fish.make_sound())


# Change behaviour in subclasses by overrriding methods
class Lion(Animal):
    def make_sound(self) -> str:
        return f"The fierce lion let's out a big {self.sound}!!!!!!"

class Canary(Animal):
    def make_sound(self) -> str:
        sound = "The canary tries to impress his partner with a song from the soul."
        sound += f"{self.sound} {self.sound} {self.sound}."
        return sound

class Goldfish(Animal):
    def make_sound(self) -> str:
        return f"{self.sound} {self.sound}...................  {self.sound}"

animals = [Lion("rawr"), Canary("tweet"), Goldfish("blub")]
for animal in animals:
    print(animal.make_sound())



# Extend classes by adding attributes and using super()
class Lion(Animal):

    def __init__(self) -> None:
        super().__init__("rawr")
        self.weight = "300kg"


    def make_sound(self) -> str:
        # Just like in __init__ we can keep the bahaviour of our
        # parent method by calling super().
        sound = super().make_sound()
        sound += f"\nThe fierce lion let's out a big {self.sound}!!!!!!"
        return sound

class Canary(Animal, ):
    def __init__(self) -> None:
        super().__init__("tweet")
        self.colour = "Orange"

    def make_sound(self) -> str:
        sound = "The canary tries to impress his partner with a song from the soul."
        sound += f"{self.sound} {self.sound} {self.sound}."
        return sound

class Goldfish(Animal):
    def __init__(self) -> None:
        super().__init__("blub")
        self.classification = "Fantail"

    def make_sound(self) -> str:
        return f"{self.sound} {self.sound}...................  {self.sound}"


lion = Lion()
bird = Canary()
fish = Goldfish()

print(lion.weight)
print(bird.colour)
print(fish.classification)


# If we wanted to we could have recieved the values of our other attributes
# from the constructor as a parameter. Let's change the Canary to show this.
class Canary(Animal, ):
    def __init__(self, colour) -> None:
        super().__init__("tweet")
        self.colour = colour

    def make_sound(self) -> str:
        sound = "The canary tries to impress his partner with a song from the soul."
        sound += f"{self.sound} {self.sound} {self.sound}."
        return sound

bird = Canary("Bright Orange")
print(bird.colour)


# Now that we know a bit more about inheritance and how it works, let's
# take it a step further and have a class inherit from two parent classes.
import time
class Printer:
    def start_print(self):
        time.sleep(1)
        for i in range(3):
            print("Printing")
            time.sleep(1)
        print("Done!")

class Scanner:
    def Scan(self):
        print("Scanner noises... chhhhchhhchhh Scan Complete.")

class ModernPrinter(Printer, Scanner):
    pass

new_printer = ModernPrinter()
new_printer.start_print()
new_printer.Scan()


# What if we had attributes to inherit and we need an __init__?
class Printer:
    def __init__(self, pages_left) -> None:
        self.pages_left = pages_left

    def start_print(self) -> None:
        time.sleep(1)
        for i in range(3):
            print("Printing")
            time.sleep(1)
        print("Done!")

class Scanner:
    def __init__(self, pages_scanned) -> None:
        self.pages_scanned = pages_scanned

    def Scan(self):
        print("Scanner noises... chhhhchhhchhh Scan Complete.")

class ModernPrinter(Printer, Scanner):
    def __init__(self) -> None:
        # super() will refrence back to the first parent class we assigned
        # In this case it is Printer.
        super().__init__(100)
        Scanner.__init__(self, 1000)

new_printer = ModernPrinter()
print(f"Pages Left: {new_printer.pages_left}")
print(f"Pages Scanned: {new_printer.pages_scanned}")

# Special Methods
# __init__ and adding string representation.
class Student:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        return f"Fullname: {self.name} {self.surname}\nAge: {self.age}"
    
    def __repr__(self):
        return f"Student({self.name}, {self.surname}, {self.age})"
    

# Operator Overloading
class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def __add__(self, other):
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)
    
    def __sub__(self, other):
        new_length = self.length - other.length
        if new_length < 0: new_length = 0
        new_width = self.width - other.width
        if new_width < 0: new_width = 0
        return Rectangle(new_length, new_width)
    
    def __str__(self) -> str:
        return f"Length: {self.length}\nWidth {self.width}"

rect1 = Rectangle(5, 7)
rect2 = Rectangle(4, 9)
# rect3  = rect1__add__(rect2)
rect3 = rect1 + rect2
print(rect3)

# Container-like behaviour.
class BookShelf:

    def __init__(self, shelf_num, shelf_genre) -> None:
        self.shelf_num = shelf_num
        self.shelf_genre = shelf_genre
        self.books = []

    def __getitem__(self, key):
        return self.books[key]
    
    def __len__(self):
        return len(self.books)
    
    def __contains__(self, item):
        return item in self.books


# Polymorphism
# print() is an examples of polymorphism as it does not care about
# the type of object it is receiving.
print("Hello")
print(3.14)
print(100)
print(True)


# Implementing polymorphism using mehtod overriding.
# Let's go back to our animals and see what polymorphism means.
class Lion(Animal):
    def __init__(self) -> None:
        super().__init__("rawr")

    def make_sound(self) -> str:
        return f"The fierce lion let's out a big {self.sound}!!!!!!"

class Canary(Animal):
    def __init__(self) -> None:
        super().__init__("tweet")

    def make_sound(self) -> str:
        sound = "The canary tries to impress his partner with a song from the soul."
        sound += f"{self.sound} {self.sound} {self.sound}."
        return sound

class Goldfish(Animal):
    def __init__(self) -> None:
        super().__init__("blub")

    def make_sound(self) -> str:
        return f"{self.sound} {self.sound}...................  {self.sound}"

# Pay attention to the return values of all the make_sound() functions
# Let's create a function that will make use of this behaviour.
def sound(sound_object):
    print(sound_object.make_sound())

# With all our make_sound funtions returning the same value none of them
# will break our function when parsed as an argument.
animals = [Lion(), Canary(), Goldfish()]
for animal in animals:
    sound(animal)

# What if we don't return the correct value type.
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("woof")
    def make_sound(self) -> None:
        print(f"{self.sound} {self.sound} {self.sound}")

dog = Dog()
sound(dog)


# Duck typing
# If it walk like a duck, swims like a duck and quacks like a duck
# then it might just be a duck.
class Student:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def make_sound(self):
        return f"Hi, I'm {self.name} {self.surname}. I am {self.age} years old!"

student = Student("Jack", "Sparrow", 38)
sound(student)