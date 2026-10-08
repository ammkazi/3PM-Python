# Terminal Todo App

print(f"{'======':^15} Terminal ToDo App     {'======':^15}")

tasks = []

while True:
    print("1. Add a new task.")
    print("2. View task list.")
    print("3. Mark a task as completed. ")
    print("4. Remove a task.")
    print("5. Exit :(")
    print()
    user_input = input("Enter your choice: ")

    if user_input == "5":
        print(f"{"======":^20} Exiting program {"======":^20}")
        break

    if user_input not in ["1", "2", "3", "4", "5"]:
        print("\nInvalid action. Please enter a valid option.")
        continue

    match user_input:
        # Enter new task
        case "1":
            new_task = input("\nEnter new task: ")

            if new_task == "":
                print("\nTask cannot be empty.")
            else:
                tasks.append(new_task)
                print("Task added successfully.")
                print("\n")

        # View all tasks

        case "2":
            if len(tasks) == 0:
                print("\nNo tasks available.")
            else:
                print("\nTasks: ")

                for index, task in enumerate(tasks, start = 1):
                    print(f"{index} - {task}")
                print()

        #Mark a task as completed.
        case "3":
            if len(tasks) == 0:
                print("\nNo tasks available.")
            else:
                print("\nTasks: ")

                for index, task in enumerate(tasks, start=1):
                    # Display task number and task
                    print(f"{index} - {task}")
                task_index = input("\nEnter task index to mark completed: ")

                task_index = int(task_index) - 1

                if 0 <= task_index < len(tasks):
                    tasks[task_index] = "[DONE]" + tasks[task_index]
                    print("\nTask marked as completed.")
                else:
                    # The entered index does not exist
                    print("\nTask does not exist.")


        # Remove a task
        case "4":
            if len(tasks) == 0:
                print("\nNo tasks available.")
            else:
                print("\nTasks:")

                # Display all tasks
                for index, item in enumerate(tasks, start=1):
                    # Display index and task
                    print(f"{index} - {item}")

                task_index = input("\nEnter task index to remove: ")
                task_index = int(task_index) - 1

                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)

                    print(f"\nTask: '{removed_task}' removed successfully.")

                else:
                    # The entered index does not exist
                    print("\nTask does not exist.")


            
        