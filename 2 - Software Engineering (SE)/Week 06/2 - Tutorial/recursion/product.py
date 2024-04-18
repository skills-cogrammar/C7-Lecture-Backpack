class Product:

    """
    Give a recursive algorithm to compute the product of two positive integers,
    m and n, using only addition and subtraction."
    """

    def __init__(self):
        return None  # Constructor method, returns None

    def product(self, a, b):
        # Recursive function to compute the product of two positive integers a and b
        if b != 0:
            return a + (self.product(a, b - 1))  # Recursively call product and add a
        return 0  # Base case: if b is 0, return 0

    def product_normal(self, a, b):
        # Function to compute the product of two positive integers using multiplication
        return a * b

    def product_iterative(self, a, b):
        # Function to compute the product of two positive integers using iteration
        prod = 0
        for _ in range(0, b):
            prod = a + prod  # Add a to prod b times
        return prod

# Testing the recursive product function
print(Product().product(3, 2))
