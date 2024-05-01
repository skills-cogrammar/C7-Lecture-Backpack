import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.expression = ""
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def add_to_expression(self, value):
        self.expression += str(value)

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error"
        return x / y

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            # result = 0
            # for operator, operation_func in self.operations.items():
            #     if operator in self.expression:
            #         # Extracting operands from the string (assuming operands are separated by the operator)
            #         operands = self.expression.split(operator)
            #         for oper in operands:
            #             result = operation_func(int(oper), result)
            # self.expression = str(result)
        except Exception as _:
            self.expression = "Error"

    def clear_expression(self):
        self.expression = ""

class Button(ttk.Button):
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command)

class CalculatorGUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.calculator = Calculator()
        self.title("HyperionDev Simple Calculator")
        self.geometry("700x400")

        self.display = tk.Entry(self, font=('Calibri', 50), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("/", 3, 3),
            ("0", 4, 0), ("C", 4, 1), (".", 4, 2), ("=", 4, 3)
        ]

        for btn_text, row, col in buttons:
            btn = Button(self, text=btn_text, command=self.create_button_command(btn_text))
            btn.grid(row=row, column=col, sticky="nsew")

        for i in range(1, 5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def create_button_command(self, text: str) -> None:
        """Create a command function for a button."""
        def command() -> None:
            self.on_button_click(text)
        return command

    def on_button_click(self, text: str) -> None:
        if text == "C":
            self.calculator.clear_expression()
        elif text == "=":
            self.calculator.calculate()
        else:
            self.calculator.add_to_expression(text)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.calculator.expression)

if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
