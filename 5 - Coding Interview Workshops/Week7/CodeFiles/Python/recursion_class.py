# Define a class named BaseClassRecursion.
class BaseClassRecursion:
    # Define a method called __init__ (short for "initialize").
    # This method is automatically called when a new object of this class is created.
    def __init__(self, number, name=None):
        # Assign the value passed to the 'number' parameter to the 'number' attribute of the object.
        self.number = number
        # Assign the value passed to the 'name' parameter to the 'name' attribute of the object.
        # If no 'name' is provided (it's None), the default value will be used.
        self.name = name

    # Define a method called __str__ (short for "string").
    # This method is called when you use the 'print' function or when an object is converted to a string.
    def __str__(self):
        # Return a string representation of the object.
        # The string will include the phrase "Parent: recursion" and the value of the 'name' attribute.
        return (f"Parent: recursion, child: {self.name}")


# Define a new class named Factorial, which inherits from the BaseClassRecursion class.
class Factorial(BaseClassRecursion):
    # Define an initializer method for the Factorial class.
    # This method is automatically called when a new object of this class is created.
    def __init__(self, number, name=None):
        # Call the initializer of the parent class (BaseClassRecursion) to set up inherited attributes.
        super().__init__(number, name)
        # Set the 'name' attribute of the object to "Factorial".
        self.name = "Factorial"

    # Define a method to calculate the factorial using tail recursion.
    def tail_factorial(self):
        # Call the private method '_tail_factorial' to perform the tail-recursive factorial calculation.
        return self._tail_factorial(self.number)

    # Define a private method for tail-recursive factorial calculation.
    def _tail_factorial(self, current_number, previous_multiplication=1):
        # Check if the current_number has reached or surpassed 0.
        if current_number <= 0:
            # If so, return the accumulated multiplication result.
            return previous_multiplication
        else:
            # If not, continue the recursion by multiplying the current number with the previous result.
            return self._tail_factorial(current_number - 1, current_number * previous_multiplication)

    # Define a method to calculate the factorial using standard recursion.
    def recursive_factorial(self):
        # Call the private method '_rec_factorial' to perform the recursive factorial calculation.
        return self._rec_factorial(self.number)

    # Define a private method for standard recursive factorial calculation.
    def _rec_factorial(self, current_number):
        # Check if the current_number has reached or surpassed 0.
        if current_number <= 0:
            # If so, return 1 (base case for factorial).
            return 1
        else:
            # If not, continue the recursion by multiplying the current number with the factorial of (current_number - 1).
            return current_number * self._rec_factorial(current_number - 1)

    # Define a method to calculate the factorial using iteration (non-recursive).
    def iter_factorial(self):
        # Call the private method '_iter_factorial' to perform the iterative factorial calculation.
        return self._iter_factorial(self.number)

    # Define a private method for iterative factorial calculation.
    def _iter_factorial(self, current_number):
        # Initialize a variable 'fact' to store the factorial result, starting with 1.
        fact = 1
        # Iterate through numbers from 'current_number' down to 1.
        while current_number > 0:
            # Multiply 'fact' by 'current_number' and decrement 'current_number'.
            fact = fact * current_number
            current_number = current_number - 1
        # Return the final factorial result.
        return fact

# Define a new class named Addition, which inherits from the BaseClassRecursion class.
class Addition(BaseClassRecursion):
    # Define an initializer method for the Addition class.
    # This method is automatically called when a new object of this class is created.
    def __init__(self, number, name=None):
        # Call the initializer of the parent class (BaseClassRecursion) to set up inherited attributes.
        super().__init__(number, name)
        # Set the 'name' attribute of the object to "Addition".
        self.name = "Addition"

    # Define a method to calculate the sum recursively.
    def recursive_sum(self):
        # Call the private method '_recursive_sum' to perform the recursive summation.
        return self._recursive_sum(self.number)

    # Define a private method for recursive summation.
    def _recursive_sum(self, current_number):
        # Check if the current number has reached 0.
        if current_number == 0:
            # If so, return 0 (base case for addition).
            return 0
        else:
            # If not, add the current number to the sum of numbers from 1 to (current_number - 1).
            return current_number + self._recursive_sum(current_number - 1)

    # Define a method to calculate the sum using tail recursion.
    def tail_recursive_sum(self):
        # Call the private method '_tail_recursive_sum' to perform the tail-recursive summation.
        return self._tail_recursive_sum(self.number)

    # Define a private method for tail-recursive summation.
    def _tail_recursive_sum(self, current_number, running_total=0):
        # Check if the current number has reached 0.
        if current_number == 0:
            # If so, return the running total.
            return running_total
        else:
            # If not, add the current number to the running total and continue the recursion.
            return self._tail_recursive_sum(current_number - 1, running_total + current_number)

    # Define a method to calculate the sum using iteration (non-recursive).
    def iter_sum(self):
        # Call the private method '_iter_sum' to perform the iterative summation.
        return self._iter_sum(self.number)

    # Define a private method for iterative summation.
    def _iter_sum(self, current_number):
        # Initialize a variable 'summ' to store the sum, starting with 0.
        summ = 0
        # Iterate through numbers from 'current_number' down to 1.
        while current_number > 0:
            # Add 'current_number' to the sum and decrement 'current_number'.
            summ = summ + current_number
            current_number = current_number - 1
        # Return the final sum.
        return summ


# Create an object 'factorial_obj' of the Factorial class with the number 5.
factorial_obj = Factorial(5)
# Create an object 'sum_obj' of the Addition class with the number 10.
sum_obj = Addition(10)

# Print a string representation of the 'factorial_obj' object.
print(factorial_obj)
# Print a string representation of the 'sum_obj' object.
print(sum_obj)

# Calculate the factorial of 5 using tail recursion and print the result.
print(factorial_obj.tail_factorial())
# Calculate the factorial of 5 using standard recursion and print the result.
print(factorial_obj.recursive_factorial())
# Calculate the factorial of 5 using standard recursion again and print the result.
print(factorial_obj.recursive_factorial())

# Calculate the sum from 1 to 10 using tail recursion and print the result.
print(sum_obj.tail_recursive_sum())
# Calculate the sum from 1 to 10 using standard recursion and print the result.
print(sum_obj.recursive_sum())
# Calculate the sum from 1 to 10 using iteration and print the result.
print(sum_obj.iter_sum())
