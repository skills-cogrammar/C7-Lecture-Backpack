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
