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
