print("~^~^~^~^~^~^~^~^~^~ Task Tracker Terminal ~^~^~^~^~^~^~^~^~^~")
tasks = []

next_id = 1

while True:
    print("\n" + "=" * 60)
    print("Taskly : A Terminal Task Manager".center(60))
    print("=" * 60)


    # Display menu options
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Change Task Status")
    print("5. List All Tasks")
    print("6. List Done Tasks")
    print("7. List Pending Tasks")
    print("8. List In-Progress Tasks")
    print("9. Search Tasks")
    print("10. Statistics")
    print("11. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "11":
        print("\nExiting Taskly : A Terminal Task Manager")
        break

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
        print("\nInvalid option. Please enter option from the given menu.")
        continue


        # Add task
    if choice == "1":
        title = input("\nEnter task description: ").strip()

        if not title:
            print("Task cannot be empty.")
            continue
        
        print("\nSet Priority: ")
        print("1. HIGH")
        print("2. MEDIUM")
        print("3. LOW")
    
        priority_choice = input("Choose priority: ").strip()
    
        if priority_choice == "1":
            priority = "HIGH"
        elif priority_choice == "2":
            priority = "MEDIUM"
        elif priority_choice == "3":
            priority = "LOW"
        else:
            priority = "MEDIUM"
    
        task = {
            "id" : next_id,
            "title" : title,
            "priority" : priority,
            "status" : "PENDING" 
        }
    
        tasks.append(task)
        print(f"\nTask #{next_id} added successfully with {priority} priority.")
    
        next_id += 1

    # Update task

    elif choice == "2":
        if len(tasks) == 0:
            print("\nNo tasks available.")
            continue

        # Display tasks
        print("\nTasks: ")

        for task in tasks:
            print(f"{task["id"]} - {task["title"]} [{task["status"]}] ")

        task_id = input("\nEnter task ID to update: ").strip()
        selected = [task for task in tasks if str(task["id"]) == task_id]

        if len(selected) == 0:
            print("\nTask does not exists.")
            continue

        task = selected[0]

        new_title = input("\nEnter a new title: ").strip()

        if not new_title:
            print("\nTask cannot be empty.")
            continue

        task["title"] = new_title

        print(f"\nTask #{task_id} updated successfully.")

    # 3. DELETE Task
    elif choice == "3":
    
            # Check whether there are tasks
        if len(tasks) == 0:
    
            print("\nNo tasks available.")
            continue

        for task in tasks:
            print(f"{task["id"]} - {task["title"]} [{task["status"]}] ")

        task_id = input("\nEnter task ID to delete: ").strip()
        new_tasks = [
            task
            for task in tasks
            if str(task["id"]) != task_id
        ]

        if len(new_tasks) < len(tasks):

            tasks = new_tasks
            print(f"\nTask #{task_id} deleted successfully.")
        else:
            print("\nTask does not exist.")

    # 4. Change Status
    elif choice == "4":
        
        if len(tasks) == 0:
            print("\nNo tasks available.")
            continue

        print("\nTasks:")
        
        for task in tasks:
            print(f"{task['id']} - {task['title']} [{task['status']}]")

        task_id = input("\nEnter task ID to change its status: ").strip()
        selected = [task for task in tasks if str(task["id"]) == task_id]

        if len(selected) == 0:
            print("\nTask does not exist.")
            continue
        task = selected[0]

        print("\nChoose new status:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Done")

        status_choice = input("\nEnter choice: ").strip()

        if status_choice == "1":

            task["status"] = "PENDING"

        elif status_choice == "2":

            task["status"] = "IN PROGRESS"

        elif status_choice == "3":

            task["status"] = "DONE"

        else:

            print("\nInvalid status.")
            continue

        print(f"\nTask #{task_id} status changed to {task["status"]}.")

        
        
        
        