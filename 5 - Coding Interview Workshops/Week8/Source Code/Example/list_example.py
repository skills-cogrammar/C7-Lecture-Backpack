import pickle

def load_tasks():
    try:
        with open("tasks.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            print("Tasks:")
            for task in tasks:
                print(task)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()