# tests/test_task.py

import unittest
import os
from models.task import Task
from data.data_access import load_tasks, save_tasks, add_task


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task = Task(1, "Task 1", "Description of Task 1", False)
        self.tasks_file = 'tasks.txt'

    def tearDown(self):
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
        self.assertEqual(len(tasks), 1) # Will give error: Open line in tasks.txt = 2 tasks
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
