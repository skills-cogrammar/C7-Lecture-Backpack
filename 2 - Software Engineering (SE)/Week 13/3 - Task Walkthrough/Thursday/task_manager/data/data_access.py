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
