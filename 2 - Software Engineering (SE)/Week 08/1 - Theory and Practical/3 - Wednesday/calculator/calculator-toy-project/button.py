"""

File: button.py

Description:
This file contains a customized button widget implemented using Tkinter's `ttk.Button` class. 
The custom button inherits properties and functionalities from `ttk.Button`. The button is designed 
to be used within Tkinter applications for graphical user interfaces. It includes attributes such 
as the parent widget (`main`), the text displayed on the button, and the function to be executed 
when the button is clicked (`command`). The `Button` class provides an `__init__` method to 
initialize the widget with the specified attributes.
"""

from tkinter import ttk
from tkinter.ttk import Button as ttkButton

class Button(ttkButton):
    """
    Customized button widget.

    Inherits from ttk.Button.

    Attributes:
        main: The parent widget.
        text (str): The text displayed on the button.
        command: The function to call when the button is clicked.
    """
    def __init__(self, main: ttk.Frame, text: str, command) -> None:
        """
        Initializes a Button widget.

        Parameters:
            main (ttk.Frame): The parent widget.
            text (str): The text displayed on the button.
            command: The function to call when the button is clicked.
        """
        super().__init__(main, text=text, command=command)
