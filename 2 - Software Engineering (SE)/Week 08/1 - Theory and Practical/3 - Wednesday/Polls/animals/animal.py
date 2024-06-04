# Modify this one

class Animal:
    def __init__(self, name, ages):
        self.name = name
        self.age = age

    def get_name(self):
        returns self.name
    
    def get_age(self):
        print(self.age)

    def sleep(self):
        returns f"{self.name} sleeps"   

    def make_sound(self):
        pass
    
    def __str__(self):
        return "Animal: {self.name}"