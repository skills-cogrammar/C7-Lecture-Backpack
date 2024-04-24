# Example 1
class MathUtil:
    """
        The `add` function is a static method in Python that takes two parameters `x` and `y` and returns
        their sum.
        
        :param x: The parameter x is the first number that will be added
        
        :param y: The `add` method defined above takes two parameters, `x` and `y`. In this context, `y`
        is the second number that will be added to the first number `x`
        
        :return: The `add` method is returning the sum of the two input parameters `x` and `y`.
        """
    @staticmethod
    def add(x, y):
        """
        The function "add" takes two parameters, x and y, and returns their sum.
        
        :param x: The `add` function you provided takes two parameters, `x` and `y`, and returns the sum
        of these two parameters
    
        :param y: The `add` function you provided takes two parameters, `x` and `y`, and returns the sum
        of these two parameters. In the context you provided, `y` is the second parameter that will be
        added to `x`
        
        :return: The function `add` is returning the sum of the two input parameters `x` and `y`.
        """
        return x + y


# The code `result = MathUtil.add(4, 5)` is calling the static method `add` from the `MathUtil` class
# with arguments `4` and `5`. This method adds the two numbers together and returns the result.
result = MathUtil.add(4, 5)
print(f"Result of {4} + {5} = {result}")


# Example 2
# The class `KameDBZ` contains a static method `kamehameha` that multiplies the input power level by
# 10.
class KameDBZ:
    """
        The `kamehameha` function is a static method in Python that multiplies the input `power_level`
        by 10.
        
        :param power_level: The `power_level` parameter represents the strength or power level of the
        Kamehameha attack. The `kamehameha` method is a static method that takes the power level as
        input and returns the result of multiplying the power level by 10
        
        :return: The `kamehameha` method is returning the result of multiplying the `power_level`
        parameter by 10.
        """
    @staticmethod
    def kamehameha(power_level):
        return power_level * 10


# The line `goku_level = 9000` is assigning the value `9000` to the variable `goku_level`. In this
# context, `goku_level` represents the power level of Goku, a character from the Dragon Ball Z series.
# This value is then used as an input parameter when calling the static method `kamehameha` from the
# `KameDBZ` class to calculate the damage caused by Goku's attack.
goku_level = 9000

# The line `damage_by_goku = KameDBZ.kamehameha(goku_level)` is calling the static method `kamehameha`
# from the `KameDBZ` class with the `goku_level` variable as an argument. This method takes the power
# level represented by `goku_level` and multiplies it by 10, returning the result. The variable
# `damage_by_goku` then stores this calculated value, representing the damage caused by Goku's attack
# after applying the Kamehameha technique.
damage_by_goku = KameDBZ.kamehameha(goku_level)

# The line `print(f"Damaged caused: {damage_by_goku}")` is displaying the result of the damage caused
# by Goku's attack after applying the Kamehameha technique. It uses f-string formatting in Python to
# insert the value of the `damage_by_goku` variable into the string for output. This allows the
# program to show the calculated damage value in the console or output window when the script is
# executed.
print(f"Damaged caused: {damage_by_goku}")
