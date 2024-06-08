"""
Example of classes, objects, and inheritance.
"""

class Cat:
    
    def __init__(self, name, legs = 4, colour = 'black'):
        """Initialise a cat object.
        
        """
        
        self.name=name
        self.legs=legs
        self.colour=colour
        
        
    def speak(self):
        """The cat makes a noise.
        
        """
        print("Meow")
        
        
    def describe(self):
        """Prints a description of the cat.
        
        """
        print("My name is %s, I have %d legs and %s fur.\n" % (self.name, self.legs, self.colour))
        
        
#-------------------------------------------------------------------------------------------------------------
class Lion(Cat):
    """Lions inherit all properties of Cats, but we can override functions, or add new ones.
    
    """
    
    def __init__(self, name):
        """Makes a lion.
        
        """
        
        self.name=name
        self.legs=4
        self.colour="yellow"
        
        
    def speak(self):
        """Lions roar.
        
        """
        print("Roar!")

        
#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    mittens=Cat("Mittens")
    fluffy=Cat("Fluffy", legs = 3, colour = "white")
    simba=Lion("Simba")
    
    mittens.speak()
    mittens.describe()
    fluffy.speak()
    fluffy.describe()
    simba.speak()
    simba.describe()