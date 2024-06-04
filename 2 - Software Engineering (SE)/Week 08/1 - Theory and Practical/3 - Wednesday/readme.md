# Setting Up Python Virtual Environment

This guide will walk you through setting up a Python virtual environment on various operating systems: Windows, Linux, and macOS. Using virtual environments is a best practice for Python development as it helps in isolating project dependencies.

## Why Use Virtual Environments?

When working on Python projects, it's common to use various libraries and packages. However, installing these dependencies directly onto your system can lead to conflicts between projects or even with system-level packages. This is where virtual environments come in handy!

A virtual environment is like a sandbox for your project. It provides an isolated space where you can install and manage dependencies without affecting other projects or your system's Python setup. Think of it as having your own clean workspace for each project!


## Windows

### Prerequisites
- Python installed on your system. If not, download and install Python from the [official Python website](https://www.python.org/downloads/).

### Steps
1. Open Command Prompt by searching for "cmd" in the Start menu.
2. Navigate to your project directory using the `cd` command.
3. Run the following command to create a virtual environment:
```bash
python -m venv custom_venv
```
4. Activate the virtual environment by running:
```bash
custom_venv\Scripts\activate
```
5. You will see `(custom_venv)` at the beginning of the command prompt, indicating that the virtual environment is activated.
## Using the Virtual Environment

Once the virtual environment is activated, you can install Python packages using `pip`. For example:
```bash
pip install package_name
```
To deactivate the virtual environment, simply run:
```bash
venv\Scripts\deactivate
```

## Linux / macOS

### Prerequisites
- Python installed on your system. Most Linux distributions and macOS come with Python pre-installed. If not, install Python using your package manager or from the [official Python website](https://www.python.org/downloads/).

### Steps
1. Open a terminal.
2. Navigate to your project directory using the `cd` command.
3. Run the following command to create a virtual environment:
```bash
python3 -m venv custom_venv
```
or 
```bash
python -m venv custom_venv
```
If you have multiple versions of Python installed, replace `python3` with the appropriate version.
4. Activate the virtual environment by running:
```bash
source custom_venv/bin/activate
```
5. You will see `(custom_venv)` at the beginning of the command prompt, indicating that the virtual environment is activated.

## Using the Virtual Environment

Once the virtual environment is activated, you can install Python packages using `pip`. For example:
```bash
pip install package_name
```

To deactivate the virtual environment, simply run:
```bash
deactivate
```

------------------------------------------------------------------------------------------------------

# Activating Virtual Environment in Visual Studio Code (VSCode)

## Introduction

Activating a virtual environment in Visual Studio Code (VSCode) allows you to work on Python projects within an isolated environment. This helps manage project dependencies and ensures that the packages installed for one project do not interfere with those of another. In this guide, we'll walk you through the steps to activate a virtual environment in VSCode.

## Prerequisites

Before you begin, ensure that you have the following installed:
- [Visual Studio Code](https://code.visualstudio.com/): An integrated development environment (IDE) by Microsoft.
- Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Extensions

To enhance your Python development experience in VSCode, we recommend installing the following extensions:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): Provides rich Python language support, including syntax highlighting, IntelliSense, and debugging capabilities.
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy): Adds support for debugging Python code within VSCode.

## Activating Virtual Environment

Follow these steps to activate a virtual environment in VSCode:

1. Open your Python project folder in VSCode.
2. Open the integrated terminal in VSCode by selecting View > Terminal from the top menu or pressing `Ctrl + `.
3. In the terminal, navigate to your project directory if you haven't already.
4. Run the following command to create a virtual environment (if you haven't already created one):
```bash
python -m venv custom_venv
```
5. Once the virtual environment is created, you need to activate it:
- On Windows:
  ```
  .\custom_venv\Scripts\activate
  ```
- On Linux/Mac:
  ```
  source custom_venv/bin/activate
  ```
You'll see `(custom_venv)` at the beginning of the command prompt, indicating that the virtual environment is activated.

6. With the virtual environment activated, you can now work on your Python project with isolated dependencies.

## Changing Between Virtual Environments

If you work on multiple Python projects with different virtual environments in VSCode, you can quickly switch between them using the following shortcuts:
- `Ctrl + Shift + P` to open the command palette.
- Type "Python: Select Interpreter" and press Enter.
- Choose the desired Python interpreter from the list of available virtual environments.

Alternatively, you can check and change the Python interpreter from the status bar:
- Look at the bottom-left corner of the VSCode window to find the current Python interpreter. Click on it to see a list of available interpreters, and select the one you want to use for your project.


## Conclusion

Activating a virtual environment in Visual Studio Code is a crucial step for Python development, as it helps manage project dependencies and ensures a clean environment for each project. By following the steps outlined in this guide and installing the recommended extensions, you'll be able to streamline your Python development workflow in VSCode.



