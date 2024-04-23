# Very bad monolithic Python code for a calculator

def calculate(operation, x, y):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            return "Error: Division by zero"
        else:
            return x / y
    else:
        return "Error: Invalid operation"

print(calculate("add", 5, 3))
print(calculate("subtract", 5, 3))
print(calculate("multiply", 5, 3))
print(calculate("divide", 5, 0))


# calculator_service.py
class CalculatorService:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        else:
            return x / y


# client.py
from calculator_service import CalculatorService

calculator_service = CalculatorService()
print(calculator_service.add(5, 3))
print(calculator_service.subtract(5, 3))
print(calculator_service.multiply(5, 3))
print(calculator_service.divide(5, 0))
