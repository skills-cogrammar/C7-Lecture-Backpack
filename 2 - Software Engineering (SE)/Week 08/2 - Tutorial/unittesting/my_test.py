import unittest
from my_module import add, subtract

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
