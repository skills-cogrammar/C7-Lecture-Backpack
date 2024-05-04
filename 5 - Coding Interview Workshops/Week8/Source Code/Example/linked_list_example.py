import pickle

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def load_linked_list():
    try:
        with open("linked_list_data.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return LinkedList()

def save_linked_list(linked_list):
    with open("linked_list_data.pkl", "wb") as file:
        pickle.dump(linked_list, file)

def main():
    linked_list = load_linked_list()

    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            linked_list.append(task)
            save_linked_list(linked_list)
        elif choice == "2":
            print("Tasks:")
            linked_list.display()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()