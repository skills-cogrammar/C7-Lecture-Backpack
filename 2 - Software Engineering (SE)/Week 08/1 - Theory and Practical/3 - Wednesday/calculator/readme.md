# Calculator Toy Project

This repository houses a simple calculator toy project implemented using Object-Oriented Programming (OOP) principles. The project aims to demonstrate modular programming by breaking down a standalone script (`calculator_bad_design.py`) into more organized and reusable components.

## Project Description

The calculator toy project provides a graphical user interface (GUI) for performing basic arithmetic operations such as addition, subtraction, multiplication, and division. It allows users to input numbers and operators using buttons and displays the input expression along with the calculated result.

## Project Structure

The project is structured as follows:

- **calc/**: This folder contains the OOP version of the calculator.
  - **button.py**: Customized button widget implemented using Tkinter's `ttk.Button` class. It provides an `__init__` method to initialize the widget with specified attributes.
  - **calculator_gui.py**: Graphical User Interface (GUI) for the calculator. It utilizes Tkinter for GUI elements and integrates with the `Calculator` class from `calculator_logic.py` to perform calculations.
  - **calculator_logic.py**: `Calculator` class for performing basic arithmetic operations. It includes methods to add to the expression, calculate the result, and clear the expression.
  - **run_script.py**: Main script to run the calculator GUI application. It imports `CalculatorGUI` from `calculator_gui.py` and creates an instance to run the application.

- **calculator_bad_design.py**: Original standalone calculator script exhibiting poor design practices and lacking modularization.

- **hyperion_dev_calc_utils/**: Folder containing utility functions for the calculator.
  - **ops.py**: Provides basic mathematical operations such as addition, subtraction, multiplication, and division.
  - **test_ops.py**: Unit tests for the mathematical operations provided in `ops.py`.

## Installation

To set up the project environment, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/calculator-toy-project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd calculator-toy-project
   ```

3. Create a Python virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Scripts

To run the scripts:

1. First, execute `calculator_bad_design.py`:

   ```bash
   python calculator_bad_design.py
   ```

   This will run the original standalone calculator script.

2. Then, navigate to the `calc/` folder:

   ```bash
   cd calc
   ```

3. Execute `run_script.py`:

   ```bash
   python run_script.py
   ```

   This will launch the calculator GUI application, allowing you to perform arithmetic operations using the graphical interface.

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
