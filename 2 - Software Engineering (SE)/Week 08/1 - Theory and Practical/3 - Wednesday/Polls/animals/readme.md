# Modules: Poll 1 - Extra Activity

## Your Mission

You've been presented with a series of Python files, each containing intentional errors. Your mission, should you choose to accept it, is to identify and fix these errors to make the code functional. Don't worry if you're new to debugging – learning to fix errors is an essential skill for any programmer.

## How to Proceed

1. **Read Carefully**: Take your time to read through each file and understand its purpose and structure.

2. **Identify Errors**: Look for any syntax errors, logical mistakes, or incorrect variable usage.

3. **Use Stack Traces**: Pay close attention to any stack traces provided when running the code. These error messages contain valuable clues about what went wrong.

4. **Experiment**: Don't be afraid to experiment with different solutions. Python is a forgiving language, and trial and error can often lead to the correct solution.

5. **Learn from Mistakes**: Mistakes are part of the learning process. Embrace them as opportunities to deepen your understanding of Python.

## Let's Get Started!

Take a deep breath, sharpen your problem-solving skills, and dive into the exercises. Remember, every error you fix brings you one step closer to becoming a proficient Python programmer.

Happy coding!

## Files

### 1. animal.py

This file defines the `Animal` class. Please modify this file.

### 2. cat.py

This file defines the `Cat` class. Please modify this file.

### 3. dog.py

This file defines the `Dog` class. Please modify this file.

### 4. driver.py

This is the driver script. Please don't modify this script. It works.

## Stack Trace Error Examples

Here are some common examples of Python stack trace errors:

1. **NameError**: This error occurs when a variable or function name is not defined.

   ```python
   >>> print(my_variable)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'my_variable' is not defined
   ```

2. **TypeError**: This error occurs when an operation is performed on an object of inappropriate type.

   ```python
   >>> x = "hello"
   >>> y = 5
   >>> print(x + y)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: can only concatenate str (not "int") to str
   ```

## Note

- Ensure you pay attention to the differences between using `print` and `return` statements in Python functions. Using `return` is essential to prevent functions from returning `None`.
- Except for the driver file, some files may not be working as expected. Use the provided stack trace to identify and fix errors.

---

Feel free to let somebody at HyperionDev know if you need any further modifications!