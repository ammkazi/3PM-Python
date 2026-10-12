print("~^~^~^~^~^~^~^~^~^~ Task Tracker Terminal ~^~^~^~^~^~^~^~^~^~")
tasks = []

next_id = 1

PRIORITIES = ["HIGH", "MEDIUM", "LOW"]

while True:
    print("\n" + "=" * 78)
    print("Taskly : A Terminal Task Manager".center(78))
    print("=" * 78)


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
            print("Invalid priority, MEDIUM assigned as default.")
    
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

        ordered_tasks = [
            task for priority in PRIORITIES 
            for task in tasks
            if task["priority"] == priority
        ]


        # Display tasks
        print("\n" + "=" * 78)
        print(f"{'ID':<6}"
              f"{'PRIORITY':<12}"
              f"{'STATUS':<16}"
              f"{'TASK TITLE':<44}")
        print("=" * 78)
        for task in ordered_tasks:
            print(f"{task['id']:<6}"
                  f"{task['priority']:<12}"
                  f"{task['status']:<16}"
                  f"{task['title']:<44}")
        print("=" * 78)

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

        ordered_tasks = [
                    task for priority in PRIORITIES 
                    for task in tasks
                    if task["priority"] == priority
                ]

        print(f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}")
        print("=" * 78)
        
        for task in ordered_tasks:
                    print(f"{task['id']:<6}"
                          f"{task['priority']:<12}"
                          f"{task['status']:<16}"
                          f"{task['title']:<44}")
        print("=" * 78)

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

        ordered_tasks = [
                    task
                    for priority in PRIORITIES
                    for task in tasks
                    if task["priority"] == priority
                ]
        print("\n" + "-" * 78)
        print(
                    f"{'ID':<6}"
                    f"{'PRIORITY':<12}"
                    f"{'STATUS':<16}"
                    f"{'TASK TITLE':<44}"
                )
        print("-" * 78)
        
                # Display all tasks.
        for task in ordered_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )
        
        print("-" * 78)
        
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

    # 5. List all tasks
    elif choice == "5": 
        if len(tasks) == 0:
            print("\nNo tasks available.")
            continue

        ordered_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task['priority'] == priority
        ]

        print("\nALL TASKS")
        print("-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)

        for task in ordered_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )

        print("-" * 78)

    # 6. List done tasks
    elif choice == "6":
        done_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task['priority'] == priority
            and task['status'] == "DONE"
        ]

        if len(done_tasks) == 0:
            print("\nNo completed tasks.")
            continue

        print("\nDONE TASKS")
        print("-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)
        for task in done_tasks:
                print(
                    f"{task['id']:<6}"
                    f"{task['priority']:<12}"
                    f"{task['status']:<16}"
                    f"{task['title']:<44}"
                )

        print("-" * 78) 

    # 7. List pending tasks
    elif choice == "7":
        pending_tasks = [
                task
                for priority in PRIORITIES
                for task in tasks
                if task["priority"] == priority
                and task["status"] == "PENDING"
            ]

        if len(pending_tasks) == 0:
                print("\nNo pending tasks.")
                continue

            # Display the table heading.
        print("\nPENDING TASKS")
        print("-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)

            # Display pending tasks in priority order.
        for task in pending_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )
        print("-" * 78)

    #8. LIST IN-PROGRESS TASKS

    elif choice == "8":

        # Select in-progress tasks and arrange them by priority.
        progress_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
            and task["status"] == "IN PROGRESS"
        ]   
        # Check whether any in-progress tasks exist.
        if len(progress_tasks) == 0:
            print("\nNo in-progress tasks.")
            continue    
        # Display the table heading.
        print("\nIN-PROGRESS TASKS")
        print("-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78) 
        # Display in-progress tasks in priority order.
        for task in progress_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )   
        print("-" * 78)

    #9. search tasks
    elif choice == "9":
        search = input("Enter text top search: ").strip().lower()

        matches = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task['priority'] == priority
            and search in task['title'].lower()
        ]

        if len(matches) == 0:
            print("\nNo matching tasks.")
            continue

        print(f"\n{len(matches)} matching task(s)")

        print("-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)

        # Display matching tasks in priority order.
        for task in matches:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )

        print("-" * 78)

    #10. Statistics feature
    elif choice == "10":
         # Count all tasks.
        total = len(tasks)

        # Count tasks marked DONE.
        done = len([
            task for task in tasks
            if task["status"] == "DONE"
        ])

        # Count tasks marked PENDING.
        pending = len([
            task for task in tasks
            if task["status"] == "PENDING"
        ])

        # Count tasks marked IN PROGRESS.
        progress = len([
            task for task in tasks
            if task["status"] == "IN PROGRESS"
        ])

        # Count HIGH priority tasks.
        high = len([
            task for task in tasks
            if task["priority"] == "HIGH"
        ])

        # Count MEDIUM priority tasks.
        medium = len([
            task for task in tasks
            if task["priority"] == "MEDIUM"
        ])

        # Count LOW priority tasks.
        low = len([
            task for task in tasks
            if task["priority"] == "LOW"
        ])

        # Display the statistics heading.
        print("\nTASK STATISTICS")
        print("-" * 42)

        # Display task totals and status counts.
        print(f"{'Total Tasks':<20}: {total}")
        print(f"{'Pending':<20}: {pending}")
        print(f"{'In Progress':<20}: {progress}")
        print(f"{'Done':<20}: {done}")

        # Calculate completion percentage when tasks exist.
        if total > 0:
            percentage = done / total * 100
        else:
            percentage = 0

        # Display completion percentage.
        print(f"{'Completion':<20}: {percentage:.0f}%")

        # Display the priority counts.
        print("\nPRIORITY BREAKDOWN")
        print(f"{'HIGH':<20}: {high}")
        print(f"{'MEDIUM':<20}: {medium}")
        print(f"{'LOW':<20}: {low}")

        print("-" * 42)