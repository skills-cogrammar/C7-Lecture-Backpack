""" ======== Steps to write the testing code
    - import unittest
    - import file with code to be tested
    - write the testing class
    - add the modules to do the tests
    - run unittest.main()
"""
import unittest
from testsformodules import sum_list_module       # Package / Folder name is case sensitive

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
        result = sum_list_module.sum_list(num_list)
        #Assert:
        self.assertEqual(result, 5)

    """
    We can now run the test and have a look at the result. 
    For the first test we can see that our test has run without any failure.
    """
    """
    Lets create some more tests to see if our behaviour is in fact what 
    we intend it to be. 
    """
    def test_list_add_with_two_number(self):
        #Arrange:
        num_list = [5, 10]
        #Act:
        result = sum_list_module.sum_list(num_list)
        #Assert:
        self.assertEqual(result, 15)
    """
    From our first test we saw that our behaviour returned the single value 
    when a list with one value is provided but 
    what happens with two values in our list?
    Ans: Our second test has failed indicating there is an error in our code.
    
    At closer inspection we can see that we have a logical error 
    that is preventing our test from passing. => Change =+ to +=

    Remember when we correct this error all our previous test should still pass.
    """
if __name__ == '__main__':
    unittest.main()
    