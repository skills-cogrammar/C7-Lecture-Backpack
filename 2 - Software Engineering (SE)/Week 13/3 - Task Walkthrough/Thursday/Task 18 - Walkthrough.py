# ------- Step 1a: Set Up a Virtual Environment
# Install virtualenv if not already installed:

Command: pip install virtualenv

# Create a virtual environment:

Command: virtualenv venv

# Activate the virtual environment:

# On Windows:
Command: .\venv\Scripts\activate

# On macOS/Linux:
Command: source venv/bin/activate

\# ------- Step 1b: Set Up a Virtual Environment with a package
# Install virtualenvwrapper-win (use virtualenvwrapper without the –win for Mac and Linux) :
Command: pip install virtualenvwrapper-win 
# If you are working in your VS Code terminal, change from powershell to command prompt view.
Command: mkvirtualenv tasks_env         # The tasks_env is auto activated with creation

# ------- Step 2: PEP 8 Linting
# Install flake8 for PEP 8 linting:
# Make sure that you are in your tasks_env

Command: pip install flake8

# For installing flake8, you can also go to VS Code Extentions:
    # - Search flake8
    # - Click install button
    # - flake8 will now autorun
    # - deactivate if you don't want it to run.

# ------- Step 3: Implement Task Manager Application
# Let's implement a basic task manager application based on a simple design:

# Create project structure:

Command: mkdir task_manager
Command: cd task_manager

# Create a .flake8 configuration file (optional but recommended) to enforce specific rules:
Command: type NUL > .flake8

# task_manager/.flake8

[flake8]
max-line-length = 79
ignore = E203, E266, E501, W503

"""The ignore setting in the .flake8 configuration file specifies which PEP 8 rules 
the linter should ignore when checking your code. Here's what each code means:

E203: Whitespace before ':'

This error is triggered when there is whitespace before a colon. 
This rule can be contentious, especially in slicing syntax, so it is often ignored.

E266: Too many leading # for block comment

This error is triggered when a block comment has too many leading # characters. 
For example, #### Comment instead of # Comment.

E501: Line too long (82 > 79 characters)

This error is triggered when a line exceeds the maximum line length, 
which is 79 characters by default. Many developers find the 79-character limit 
too restrictive and prefer to use a higher limit, such as 120 characters.

W503: Line break before binary operator

This warning is triggered when a line break occurs before a binary operator. 
This rule was revised in PEP 8, and now it is considered acceptable to 
break lines before binary operators. 
"""

Command: mkdir models
Command: mkdir data
Command: type NUL > models/task.py
Command: type NUL > data/data_access.py
Command: type NUL > main.py
Command: type NUL > __init__.py

# Implement the Task class in models/task.py:

# models/task.py

class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.completed}"
    
    @staticmethod
    def from_string(task_string):
        task_id, title, description, completed = task_string.strip().split(', ')
        return Task(int(task_id), title, description, completed == 'True')

# Implement file-based data access layer in data/data_access.py:

# data/data_access.py

from models.task import Task

TASKS_FILE = 'data/tasks.txt'

def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                tasks.append(Task.from_string(line))
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

# Implement the main logic in main.py:

# main.py

from models.task import Task
from data.data_access import load_tasks, save_tasks, add_task

def main():
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task_id = int(input("Enter task ID: "))
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(task_id, title, description)
            add_task(task)
        elif choice == "2":
            tasks = load_tasks()
            for task in tasks:
                print(task)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            tasks = load_tasks()
            for task in tasks:
                if task.task_id == task_id:
                    task.mark_completed()
                    print(f"Task {task_id} marked as completed.")
                    break
            else:
                print(f"No task found with ID {task_id}.")
            save_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

# ------- Step 4: Write Unit Tests
# Create a tests directory and test_task.py:

Command: mkdir tests
Command: type NUL > tests/test_task.py

# Write unit tests in tests/test_task.py:

# tests/test_task.py

import unittest
from models.task import Task
from data.data_access import load_tasks, save_tasks, add_task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task = Task(1, "Task 1", "Description of Task 1", False)
        self.tasks_file = 'data/tasks.txt'
    
    def tearDown(self):
        import os
        if os.path.exists(self.tasks_file):
            os.remove(self.tasks_file)

    def test_task_creation(self):
        self.assertEqual(self.task.task_id, 1)
        self.assertEqual(self.task.title, "Task 1")
        self.assertEqual(self.task.description, "Description of Task 1")
        self.assertFalse(self.task.completed)

    def test_add_and_load_task(self):
        add_task(self.task)  # Add the task using add_task function
        tasks = load_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].task_id, self.task.task_id)
        self.assertEqual(tasks[0].title, self.task.title)
        self.assertEqual(tasks[0].description, self.task.description)
        self.assertEqual(tasks[0].completed, self.task.completed)

    def test_mark_completed(self):
        self.task.mark_completed()
        self.assertTrue(self.task.completed)
        save_tasks([self.task])
        tasks = load_tasks()
        self.assertTrue(tasks[0].completed)

if __name__ == "__main__":
    unittest.main()

# ------- Step 5: Generate requirements.txt
# Freeze dependencies into requirements.txt:
# Go to folder where you want requirements file to be created
Command: pip freeze > requirements.txt

# Add software to requiements.txt with:
Command: echo flake8 > requirements.txt

# Running a requiements.txt with:
Command: pip install -r requirements.txt

# ------- Step 6: Running the project
# Run 'flake8' to check for PEP compliance if not installed in VS Code:
Command: flake8

# Run your applications:
Command: python main.py

# Run the unit tests:
Command: python -m unittest discover tests

# ------- Final Project Structure

task_manager/
│
├── data/
│   └── data_access.py
│
├── models/
│   └── task.py
│
├── tests/
│   └── test_task.py
│
├── __init__.py
├── main.py
├── requirements.txt
└── .flake8
