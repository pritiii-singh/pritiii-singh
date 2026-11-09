
tasks = []

while True:
    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # Add a task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"name": task, "done": False})
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available!")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Pending"
                print(f"{i}. {task['name']} - {status}")

    # Complete a task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete!")
        else:
            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["done"] = True
                print("Task completed!")
            else:
                print("Invalid task number!")

    # Delete a task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Deleted:", removed["name"])
            else:
                print("Invalid task number!")

    # Exit
    elif choice == "5":
        print("Thank you for using To-Do List App!")
        break

    else:
        print("Invalid choice! Please try again.")
