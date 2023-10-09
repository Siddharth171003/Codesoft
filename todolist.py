# Initialize an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task index")

# Main loop
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
