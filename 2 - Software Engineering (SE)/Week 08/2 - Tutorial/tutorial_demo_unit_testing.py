"""========= Python testing in Visual Studio Code

--- 1.  Create a folder for your working space / project.
        /Workspace

--- 2.  Create a another folder in the workspace and place the file 
        with the code to be tested in it.
        /modulestotest/sum_list_module.py

--- 3.  Open the python file in step 2 to make sure the correct workspace is active.

--- 4.  Make sure the Python extention is installed.
        https://marketplace.visualstudio.com/items?itemName=ms-python.python

--- 5.  Open the glass test beaker icon on the left of VS Code and choose 
        Configure Python Tests

        - If you don't see the Configure Python Tests option under the beaker icon,
            use the menu /View/Command Palette/Python: Configure Tests

        - Select the workspace <Workspace>
        - Select the test framework <unittest>
        - Select directory containing the tests code <testsformodules>
        - Select the file name pattern to identify the test files
          in the previous step directory, ie. <test_*.py> or <*_test.py>  

--- 6.  Time to create tests
        Create a filename in the testsformodules folder with name pattern
        ie. for test_*.py naming pattern - test_unittest.py

        ============ STEPS for writing unit tests using the unittest framework
        a. Import the unittest module.
        b. Import file with code to be tested.
        c. Create a test class that inherits from unittest.TestCase.
        d. Write test methods within the test class, where 
           each method represents a specific test case.
        e. Use various assertion methods(ie. assertEqual) provided by the unittest.TestCase 
           class to check the expected outcomes of your code.
        f. Optionally, set up and tear down code that needs to run before 
           and after each test using setUp() and tearDown() methods.
        g. run unittest.main()

--- 7.  Test Discovery
        The discovered tests will show under the beaker icon.

        If discovery failed, you can see the errors in the terminal under the 
        OUTPUT TAB with Python selected in the dropdown list.

        For multi-level folders, a blank __init__.py file might need to be 
        placed in the project folder for the files to be part of the discovery.

        If you really get stuck, there are times when Visual Code have issues
        with auto-updates and a simple restart of VS might solve the issue just
        to force a reset.

--- 8.  Run Tests
        Open Test file and select green run icon next to line numbers OR
        Click run icon on individual test or on class for all the tests to run.
        Results under Menu: View/Terminal and Choose the TEST RESULTS TAB

--- 9.  Debug Tests
        Follow error messages, debug the code and repeat step 8 and 9 until
        all errors are resolved.
"""

"""
Let's take a look at some behaviour we can test using unittest. 
(Note that a unit does not necessarily mean a function but 
refers to behaviour within our program. 
Some units under test will use more than one function for its 
intended behaviour.)
"""

"""     ==========  Example 1: Testing a Package  ==========
Create sum_list() function in a separate .py file and place in /modulestotest.
"""
# =========== BELOW CODE is in test_unittest.py
import unittest
# Package / Folder name below is case sensitive
from modulestotest.sum_list_module import sum_list  

class TestExamples(unittest.TestCase):
    """
    Now to create the first test for our unit. 
    We can perform a very basic test to see if our function 
    will give us the intended result for a list with a single value.
    """
    def test_list_add_with_one_number(self):
        #Arrange:
        num_list = [5]
        #Act:
        result = sum_list(num_list)
        #Assert:
        self.assertEqual(result, 5)

    """
    We can now run the test and have a look at the result. 
    For the first test we can see that our test has run without any failure.

    Lets create some more tests to see if our behaviour is in fact what 
    we intend it to be. 
    """
    def test_list_add_with_two_number(self):
        #Arrange:
        num_list = [5, 10]
        #Act:
        result = sum_list(num_list)
        #Assert:
        self.assertEqual(result, 15)
    """
    From our first test we saw that our behaviour returned the single value 
    when a list with one value is provided but what happens with two values in our list?
    Ans: Our second test has failed indicating there is an error in our code.
    
    At closer inspection we can see that we have a logical error 
    that is preventing our test from passing. => Change =+ to +=

    Remember when we correct this error all our previous test should still pass.
    """
if __name__ == '__main__':
    unittest.main()

# ========== Code for the sum_list_module.py file
def sum_list(num_list):
    """
    Sums up the elements in a list of numbers.

    Args:
        num_list (list): A list of numbers to be summed.

    Returns:
        int: The sum of all numbers in the list.
    """
    total = 0
    for num in num_list:
        total =+ num  # Use the += operator to update total from =+ num
    return total

"""     ==========  Example 2: Testing a Module  ==========
In this example, we define a test class TestMathFunctions 
that inherits from unittest.TestCase. 
Within this class, we define test methods such as test_add and test_subtract, 
where we use assertion methods like assertEqual to check the expected results 
of the add and subtract functions from the my_module module. 
Finally, we run the tests using unittest.main().

1. Choose a different workspace / project folder.
2. Add the my_module.py(Code to be tested) file directly in the project folder.
3. Add the my_test.py(Code with the testing class) file in the project folder.
4. Click on the project folder.
5. Configure the test with 
    - Menu options View/Command Palette/Python: Configure Tests
    - Choose Project Folder
    - Choose unittest framework
    - Choose root directory
    - Choose pattern *_test.py
    - Check the settings.json file in the .vscode folder in the project folder
"""

# Code for the my_test.py file
import unittest
from my_module import add, subtract         # Importing a Module / file name

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        # Test add function with positive numbers
        self.assertEqual(add(2, 3), 5)
        
        # Test add function with negative numbers
        self.assertEqual(add(-2, -3), -5)
        
        # Test add function with one positive and one negative number
        self.assertEqual(add(2, -3), -1)
        
    def test_subtract(self):
        # Test subtract function with positive numbers
        self.assertEqual(subtract(5, 3), 2)
        
        # Test subtract function with negative numbers
        self.assertEqual(subtract(-5, -3), -2)
        
        # Test subtract function with one positive and one negative number
        self.assertEqual(subtract(5, -3), 8)

if __name__ == '__main__':
    unittest.main()

# Code for the my_module.py file
def add(x, y):
    """
    Adds two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The result of subtracting y from x.
    """
    return x - y
