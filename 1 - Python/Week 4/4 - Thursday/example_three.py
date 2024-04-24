# Example 1
class Archers:
    # The line `total_people = 0` is defining a class variable named `total_people` and initializing
    # it with a value of 0. This class variable belongs to the `Archers` class and is used to keep
    # track of the total number of instances (people) created from the `Archers` class. Each time a
    # new instance of the `Archers` class is created, this variable is incremented to reflect the
    # total count of instances.
    total_people = 0

    """
    The code defines a Python class with a constructor that increments a class
    variable and a class method to display the total count of instances 
    created.
    
    :param name: The `name` parameter is used in the `__init__` method to
    initialize the `name` attribute of an instance of the `Archers` class.
    It represents the name of a person or entity being created as an instance
    of the class
    """
    def __init__(self, name):
        """
        The function initializes an object with a name attribute and
        increments the total number of people in the Archers class.

        :param name: The `__init__` method is a special method in Python
        classes used for initializing new objects. In this case, the `__init__`
        method takes two parameters: `self` and `name`. The `self` parameter
        is a reference to the current instance of the class`
        """
        self.name = name
        Archers.total_people += 1

    @classmethod
    def display_total_people(cls):
        """
        This class method in Python displays the total number of people using a class variable.
        
        :param cls: In the context of a class method in Python, `cls` refers to the class itself. It is
        used to access class variables and methods within the class method. In the provided code
        snippet, `cls.total_people` is accessing the class variable `total_people` to display the total
        number of people
        """
        print(f"Total people: {cls.total_people}")


# The lines `archer1 = Archers("legolas")` and `archer2 = Archers("Robin hood")` are creating
# instances of the `Archers` class with the names "legolas" and "Robin hood" respectively.
archer1 = Archers("legolas")
archer2 = Archers("Robin hood")

# `Archers.display_total_people()` is a class method call that belongs to the `Archers` class in
# Python. When this method is called, it accesses the class variable `total_people` within the
# `Archers` class and prints out the total count of instances (people) created from the `Archers`
# class. In this specific example, it will print the total number of people created, which is 2, as
# two instances of the `Archers` class have been created with names "legolas" and "Robin hood".
Archers.display_total_people()
