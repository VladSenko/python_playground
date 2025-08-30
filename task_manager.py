import os

# file to store taks
FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                taks_id, title, status = line.strip().split(" | ")
                tasks[int(taks_id)] = {"title": title, "status": status}
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} \n")


def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0)+1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")


def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]['status'] = 'complete'
        print(f"Task '{tasks[task_id]['title']}' marked as complete")
    else:
        print("Task ID is not found")


def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted")
    else:
        print("Task ID is not found")


def main():
    tasks = load_tasks()
    while True:
        print("\n Task Manager Menu:")
        print("1. Add task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. EXIT")

        choice = input("Enter your choicr: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Bye!")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
