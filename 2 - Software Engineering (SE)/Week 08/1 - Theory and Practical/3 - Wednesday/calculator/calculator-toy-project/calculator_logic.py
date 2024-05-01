from hyperion_dev_calc_utils import ops

class Calculator:
    """
    Calculator class for performing basic arithmetic operations.

    Attributes:
        expression (str): The current expression to be evaluated.
        operations (dict): A dictionary mapping arithmetic operators to their corresponding functions.
    """

    def __init__(self) -> None:
        """Initialize the Calculator."""
        self.expression = ""
        self.operations = {
            '+': ops.add,
            '-': ops.subtract,
            '*': ops.multiply,
            '/': ops.divide
        }

    def add_to_expression(self, value: str) -> None:
        """
        Add a value to the expression.

        Parameters:
            value (str): The value to add to the expression.
        """
        self.expression += str(value)

    def calculate(self) -> None:
        """Evaluate the expression and update the result."""
        try:
            result = 0
            for operator, operation_func in self.operations.items():
                if operator in self.expression:
                    operands = self.expression.split(operator)
                    for oper in operands:
                        result = operation_func(result, int(oper))
            self.expression = str(result)
        except Exception:
            self.expression = "Error"

    def clear_expression(self) -> None:
        """Clear the expression."""
        self.expression = ""
