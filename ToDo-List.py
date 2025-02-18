import os

# Define file where tasks will be saved
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def show_menu():
    """Display the menu."""
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Edit task")
    print("5. Exit")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks to show!")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    """Remove a task."""
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def edit_task(tasks):
    """Edit an existing task."""
    try:
        task_number = int(input("Enter the task number to edit: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_number - 1] = new_task
            print(f"Task {task_number} updated to: '{new_task}'")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list app."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            edit_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting the To-Do list application...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
