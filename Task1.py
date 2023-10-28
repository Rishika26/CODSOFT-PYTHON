# Define the to-do list data structure (e.g., a list of dictionaries)
todo_list = []

# Function to add a task
def add_task(description, due_date):
    task = {"description": description, "due_date": due_date, "completed": False}
    todo_list.append(task)

# Function to list tasks
def list_tasks():
    for index, task in enumerate(todo_list, 1):
        status = "X" if task["completed"] else " "
        print(f"{index}. [{status}] {task['description']} (Due: {task['due_date']})")

# Function to mark a task as completed
def complete_task(task_index):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["completed"] = True
    else:
        print("Invalid task index")

# Function to remove a task
def remove_task(task_index):
    if 1 <= task_index <= len(todo_list):
        del todo_list[task_index - 1]
    else:
        print("Invalid task index")

# Main program loop
while True:
    print("\nTo-Do List:")
    list_tasks()
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        add_task(description, due_date)
    elif choice == "2":
        task_index = int(input("Enter the task index to mark as completed: "))
        complete_task(task_index)
    elif choice == "3":
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == "4":
        break
    else:
        print("Invalid choice")

print("Goodbye!")

