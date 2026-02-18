tasks = []

while True:
    print("\n--- TODO LIST MENU ---")
    print("1. Add New Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Discard All Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == 3:
        if not tasks:
            print("No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task removed.")
            else:
                print("Invalid task number.")

    elif choice == 4:
        tasks.clear()
        print("All tasks discarded.")

    elif choice == 5:
        print("Exiting Todo List Manager.")
        break

    else:
        print("Invalid choice. Try again.")