
import os

FILE_NAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("📝 No tasks in your to-do list.")
    else:
        print("\n📋 To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!\n")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"❌ Removed: {removed}\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("📌 To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
