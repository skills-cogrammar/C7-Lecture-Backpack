import timeit
import matplotlib.pyplot as plt
from linked_list_example import LinkedList

def linked_list_operations(n, operation):
    linked_list = LinkedList()
    if operation == "append":
        for i in range(n):
            linked_list.append(f"Task {i}")
    elif operation == "insert":
        linked_list.append("Initial Task")
        for i in range(n):
            linked_list.insert(0, f"Task {i}")
    elif operation == "remove":
        for i in range(n):
            linked_list.append(f"Task {i}")
        for i in range(n):
            linked_list.remove(f"Task {i}")

def list_operations(n, operation):
    tasks = []
    if operation == "append":
        for i in range(n):
            tasks.append(f"Task {i}")
    elif operation == "insert":
        tasks.append("Initial Task")
        for i in range(n):
            tasks.insert(0, f"Task {i}")
    elif operation == "remove":
        for i in range(n):
            tasks.append(f"Task {i}")
        for i in range(n):
            tasks.remove(f"Task {i}")

def plot_operations(n_values, operation):
    linked_list_times = []
    list_times = []
    for n in n_values:
        linked_list_time = timeit.timeit(lambda: linked_list_operations(n, operation), number=1)
        list_time = timeit.timeit(lambda: list_operations(n, operation), number=1)
        linked_list_times.append(linked_list_time)
        list_times.append(list_time)

    plt.figure()
    plt.plot(n_values, linked_list_times, label="Linked List")
    plt.plot(n_values, list_times, label="List")
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"{operation.capitalize()} Operation")
    plt.legend()

def main():
    n_values = [10, 100, 1000, 10000]
    operations = ["append", "insert", "remove"]

    for operation in operations:
        plot_operations(n_values, operation)

    plt.show()

if __name__ == "__main__":
    main()