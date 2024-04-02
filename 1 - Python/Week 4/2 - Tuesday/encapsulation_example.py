# The class `Car` has methods to initialize a speed attribute, accelerate the car, and retrieve the
# current speed.
# This Python class defines a Car with a private speed attribute that can be increased by 100 units
# and accessed through a method.
class Car:
    """
    This Python class defines a Car with a private speed attribute that can be
    increased by 100 units and accessed through a method."""

    def __init__(self):
        """
        The above function is a Python class constructor that initializes a
        private attribute `__speed` with a value of 1000.
        """
        self.__speed = 1000

    def accel(self):
        """
        The `accel` function increases the speed attribute of an object by 100.
        """
        self.__speed += 100

    def get_speed(self):
        """
        This function returns the speed attribute of an object.
        :return: The `get_speed` method is returning the value of the `__speed`
        attribute of the object.
        """
        return self.__speed
    

# `really_fast_car = Car()` is creating an instance of the `Car` class named `really_fast_car`. This
# instance will have its own private speed attribute initialized to 1000 when the `Car` object is
# created.
really_fast_car = Car()

# print(really_fast_car.speed)

# The `really_fast_car.accel()` method is increasing the speed attribute of the `really_fast_car`
# object by 100 units. In this case, it is increasing the speed from 1000 to 1100.
really_fast_car.accel()

# `print(really_fast_car.get_speed())` is calling the `get_speed()` method of the `really_fast_car`
# object, which returns the current speed attribute value of the car. This value is then printed to
# the console. In this specific case, it will print `1100`, as the speed was increased by 100 units
# using the `accel()` method before retrieving and printing the speed.
print(really_fast_car.get_speed())
