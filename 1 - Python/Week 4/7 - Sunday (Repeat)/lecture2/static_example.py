class MathUtil:
    """ The add function is a static method that takes two parameters
    x and y and returns their sum
    """
    @staticmethod
    def add(x,y):
        return x + y 
    
result = MathUtil.add(45,55)
print(result)    