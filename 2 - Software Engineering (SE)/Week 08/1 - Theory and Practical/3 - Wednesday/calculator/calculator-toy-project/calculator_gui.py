from calculator_logic import Calculator
from button import Button
import tkinter as tk

class CalculatorGUI(tk.Tk):
    """
    Graphical User Interface (GUI) for a simple calculator.

    Attributes:
        calculator (Calculator): An instance of the Calculator class.
        display (tk.Entry): The display widget to show the input and output.
    """

    def __init__(self) -> None:
        """Initialize the Calculator GUI."""
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
        """Handle button clicks."""
        if text == "C":
            self.calculator.clear_expression()
        elif text == "=":
            self.calculator.calculate()
        else:
            self.calculator.add_to_expression(text)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.calculator.expression)
