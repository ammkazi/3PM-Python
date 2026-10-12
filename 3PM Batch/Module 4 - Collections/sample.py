# ============================================================
# VISUAL LABS - MINI PROJECT 4.1
# TERMINAL TO-DO LIST MANAGER
# ============================================================

# Concepts used:
# Lists, Dictionaries, Strings, Variables
# if-elif-else, while loop, for loop, match-case
# break, continue, input(), print(), len(), str()
# List comprehensions, f-strings, Dictionary access
# List methods, String methods, Comparisons, Arithmetic


# Store all tasks in an empty list.
tasks = []

# Assign a unique ID to every new task.
next_id = 1

# Store the order in which priorities should be displayed.
PRIORITIES = ("HIGH", "MEDIUM", "LOW")


# Keep running until the user chooses Exit.
while True:

    # Display the application heading.
    print("\n" + "=" * 78)
    print(f"{'VISUAL LABS TO-DO MANAGER':^78}")
    print("=" * 78)

    # Display all menu options.
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

    # Ask the user to select an option.
    choice = input("\nEnter your choice: ").strip()

    # Exit the program when the user enters 11.
    if choice == "11":
        print("\nExiting To-Do Manager...")
        break

    # Reject choices that are not present in the menu.
    if choice not in [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10", "11"
    ]:
        print("\nInvalid option.")
        continue

    # --------------------------------------------------------
    # OPTION 1 - ADD TASK
    # --------------------------------------------------------

    if choice == "1":

        # Ask for the task description.
        title = input("\nEnter task: ").strip()

        # Reject an empty task title.
        if not title:
            print("Task cannot be empty.")
            continue

        # Display the available priorities.
        print("\nPriority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        # Ask the user to select a priority.
        priority_choice = input("Choose priority: ").strip()

        # Convert the selected number into a priority name.
        if priority_choice == "1":
            priority = "HIGH"
        elif priority_choice == "2":
            priority = "MEDIUM"
        elif priority_choice == "3":
            priority = "LOW"
        else:
            # Use MEDIUM when the choice is invalid.
            priority = "MEDIUM"
            print("Invalid priority. MEDIUM assigned.")

        # Create a dictionary containing the task details.
        task = {
            "id": next_id,
            "title": title,
            "priority": priority,
            "status": "PENDING"
        }

        # Add the dictionary to the task list.
        tasks.append(task)

        # Display a confirmation message.
        print(
            f"\nTask #{next_id} added successfully "
            f"with {priority} priority."
        )

        # Increase the ID for the next task.
        next_id += 1

    # --------------------------------------------------------
    # OPTION 2 - UPDATE TASK
    # --------------------------------------------------------

    elif choice == "2":

        # Check whether any tasks exist.
        if len(tasks) == 0:
            print("\nNo tasks available.")
            continue

        # Arrange tasks by HIGH, MEDIUM, then LOW priority.
        ordered_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
        ]

        # Display the table heading.
        print("\n" + "-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)

        # Display each task in priority order.
        for task in ordered_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )

        print("-" * 78)

        # Ask which task should be updated.
        task_id = input("\nEnter task ID to update: ").strip()

        # Find the task whose ID matches the user's input.
        selected = [
            task for task in tasks
            if str(task["id"]) == task_id
        ]

        # Stop this operation if the ID does not exist.
        if len(selected) == 0:
            print("\nTask does not exist.")
            continue

        # Get the matching task dictionary.
        task = selected[0]

        # Ask for the replacement title.
        new_title = input("Enter new task title: ").strip()

        # Reject an empty replacement title.
        if not new_title:
            print("Task cannot be empty.")
            continue

        # Update the title in the original dictionary.
        task["title"] = new_title

        # Confirm the update.
        print(f"\nTask #{task_id} updated successfully.")

    # --------------------------------------------------------
    # OPTION 3 - DELETE TASK
    # --------------------------------------------------------

    elif choice == "3":

        # Check whether any tasks exist.
        if len(tasks) == 0:
            print("\nNo tasks available.")
            continue

        # Arrange tasks by priority for display.
        ordered_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
        ]

        # Display the table heading.
        print("\n" + "-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)

        # Display the tasks.
        for task in ordered_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )

        print("-" * 78)

        # Ask for the ID of the task to delete.
        task_id = input("\nEnter task ID to delete: ").strip()

        # Keep every task except the one with the entered ID.
        new_tasks = [
            task for task in tasks
            if str(task["id"]) != task_id
        ]

        # Compare list lengths to check whether a task was removed.
        if len(new_tasks) < len(tasks):

            # Replace the old list with the filtered list.
            tasks = new_tasks

            # Confirm deletion.
            print(f"\nTask #{task_id} deleted successfully.")

        else:
            # No task matched the entered ID.
            print("\nTask does not exist.")

    # --------------------------------------------------------
    # OPTION 4 - CHANGE TASK STATUS
    # --------------------------------------------------------

    elif choice == "4":

        # Check whether any tasks exist.
        if len(tasks) == 0:
            print("\nNo tasks available.")
            continue

        # Arrange tasks by priority for display.
        ordered_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
        ]

        # Display the table heading.
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

        # Ask which task's status should change.
        task_id = input("\nEnter task ID: ").strip()

        # Find the task with the matching ID.
        selected = [
            task for task in tasks
            if str(task["id"]) == task_id
        ]

        # Reject an ID that does not exist.
        if len(selected) == 0:
            print("\nTask does not exist.")
            continue

        # Get the selected task.
        task = selected[0]

        # Display the available statuses.
        print("\nChoose new status:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Done")

        # Ask for the new status.
        status_choice = input("Enter choice: ").strip()

        # Update the status according to the selected option.
        if status_choice == "1":
            task["status"] = "PENDING"
        elif status_choice == "2":
            task["status"] = "IN PROGRESS"
        elif status_choice == "3":
            task["status"] = "DONE"
        else:
            # Reject an invalid status choice.
            print("\nInvalid status.")
            continue

        # Confirm the status change.
        print(
            f"\nTask #{task_id} status changed to "
            f"{task['status']}."
        )

    # --------------------------------------------------------
    # OPTION 5 - LIST ALL TASKS
    # --------------------------------------------------------

    elif choice == "5":

        # Check whether any tasks exist.
        if len(tasks) == 0:
            print("\nNo tasks available.")
            continue

        # Arrange tasks from HIGH to LOW priority.
        ordered_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
        ]

        # Display the table heading.
        print("\nALL TASKS")
        print("-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)

        # Display every task in priority order.
        for task in ordered_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )

        print("-" * 78)

    # --------------------------------------------------------
    # OPTION 6 - LIST DONE TASKS
    # --------------------------------------------------------

    elif choice == "6":

        # Select completed tasks and arrange them by priority.
        done_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
            and task["status"] == "DONE"
        ]

        # Check whether any completed tasks exist.
        if len(done_tasks) == 0:
            print("\nNo completed tasks.")
            continue

        # Display the table heading.
        print("\nDONE TASKS")
        print("-" * 78)
        print(
            f"{'ID':<6}"
            f"{'PRIORITY':<12}"
            f"{'STATUS':<16}"
            f"{'TASK TITLE':<44}"
        )
        print("-" * 78)

        # Display completed tasks in priority order.
        for task in done_tasks:
            print(
                f"{task['id']:<6}"
                f"{task['priority']:<12}"
                f"{task['status']:<16}"
                f"{task['title']:<44}"
            )

        print("-" * 78)

    # --------------------------------------------------------
    # OPTION 7 - LIST PENDING TASKS
    # --------------------------------------------------------

    elif choice == "7":

        # Select pending tasks and arrange them by priority.
        pending_tasks = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
            and task["status"] == "PENDING"
        ]

        # Check whether any pending tasks exist.
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

    # --------------------------------------------------------
    # OPTION 8 - LIST IN-PROGRESS TASKS
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # OPTION 9 - SEARCH TASKS
    # --------------------------------------------------------

    elif choice == "9":

        # Ask the user for the text to search for.
        search = input("\nEnter text to search: ").strip().lower()

        # Find matching titles and arrange results by priority.
        matches = [
            task
            for priority in PRIORITIES
            for task in tasks
            if task["priority"] == priority
            and search in task["title"].lower()
        ]

        # Check whether any matches were found.
        if len(matches) == 0:
            print("\nNo matching tasks.")
            continue

        # Display the number of matching tasks.
        print(f"\n{len(matches)} matching task(s)")

        # Display the table heading.
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

    # --------------------------------------------------------
    # OPTION 10 - STATISTICS
    # --------------------------------------------------------

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