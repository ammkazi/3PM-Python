# ============================================================
# VISUAL LABS - MINI PROJECT 4.1
# TERMINAL TO-DO LIST MANAGER
# ============================================================

# Concepts used:
# Lists
# Dictionaries
# Strings
# if-elif-else
# while loop
# for loop
# match-case
# break
# continue
# input()
# print()
# len()
# str()
# int()
# list comprehensions
# f-strings
# Dictionary methods
# List methods


# ------------------------------------------------------------
# TASK LIST
# ------------------------------------------------------------

# Empty list to store all tasks
tasks = []


# This number will be used as the unique ID
# for every new task
next_id = 1


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

# Keep showing the menu until the user chooses Exit
while True:

    # Display application heading
    print("\n" + "=" * 60)
    print("VISUAL LABS TO-DO MANAGER".center(60))
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


    # Ask the user for an option
    choice = input("\nEnter your choice: ").strip()


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if choice == "11":

        print("\nExiting To-Do Manager...")
        break


    # Check whether the menu choice is valid
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

        # Ask for task title
        title = input("\nEnter task: ").strip()


        # Do not allow an empty task
        if not title:

            print("Task cannot be empty.")
            continue


        # Display priority choices
        print("\nPriority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")


        # Ask for priority
        priority_choice = input("Choose priority: ").strip()


        # Convert priority choice into text
        if priority_choice == "1":
            priority = "HIGH"

        elif priority_choice == "2":
            priority = "MEDIUM"

        elif priority_choice == "3":
            priority = "LOW"

        else:
            # Use Medium if the user enters
            # an invalid priority
            priority = "MEDIUM"


        # Create a dictionary for the new task
        task = {
            "id": next_id,
            "title": title,
            "priority": priority,
            "status": "PENDING"
        }


        # Add the dictionary to the task list
        tasks.append(task)


        # Display confirmation
        print(
            f"\nTask #{next_id} added successfully "
            f"with {priority} priority."
        )


        # Increase ID for the next task
        next_id += 1


    # --------------------------------------------------------
    # OPTION 2 - UPDATE TASK
    # --------------------------------------------------------

    elif choice == "2":

        # Check if there are any tasks
        if len(tasks) == 0:

            print("\nNo tasks available.")
            continue


        # Display all tasks
        print("\nTasks:")

        for task in tasks:

            print(
                f"{task['id']} - "
                f"{task['title']} "
                f"[{task['status']}]"
            )


        # Ask which task should be updated
        task_id = input("\nEnter task ID to update: ").strip()


        # Create a list containing the matching task
        selected = [
            task for task in tasks
            if str(task["id"]) == task_id
        ]


        # Check whether the task exists
        if len(selected) == 0:

            print("\nTask does not exist.")
            continue


        # Get the first matching task
        task = selected[0]


        # Ask for the new title
        new_title = input(
            "\nEnter new task title: "
        ).strip()


        # Check whether the new title is empty
        if not new_title:

            print("Task cannot be empty.")
            continue


        # Update the title
        task["title"] = new_title


        # Display confirmation
        print(f"\nTask #{task_id} updated successfully.")


    # --------------------------------------------------------
    # OPTION 3 - DELETE TASK
    # --------------------------------------------------------

    elif choice == "3":

        # Check whether there are tasks
        if len(tasks) == 0:

            print("\nNo tasks available.")
            continue


        # Display all tasks
        print("\nTasks:")

        for task in tasks:

            print(
                f"{task['id']} - "
                f"{task['title']} "
                f"[{task['status']}]"
            )


        # Ask for task ID
        task_id = input(
            "\nEnter task ID to delete: "
        ).strip()


        # Create a new list containing
        # every task except the selected one
        new_tasks = [
            task for task in tasks
            if str(task["id"]) != task_id
        ]


        # Compare lengths to see whether
        # something was actually deleted
        if len(new_tasks) < len(tasks):

            tasks = new_tasks

            print(f"\nTask #{task_id} deleted successfully.")

        else:

            print("\nTask does not exist.")


    # --------------------------------------------------------
    # OPTION 4 - CHANGE TASK STATUS
    # --------------------------------------------------------

    elif choice == "4":

        # Check whether there are tasks
        if len(tasks) == 0:

            print("\nNo tasks available.")
            continue


        # Display tasks
        print("\nTasks:")

        for task in tasks:

            print(
                f"{task['id']} - "
                f"{task['title']} "
                f"[{task['status']}]"
            )


        # Ask for task ID
        task_id = input(
            "\nEnter task ID: "
        ).strip()


        # Find matching task
        selected = [
            task for task in tasks
            if str(task["id"]) == task_id
        ]


        # Check whether task exists
        if len(selected) == 0:

            print("\nTask does not exist.")
            continue


        # Get the selected task
        task = selected[0]


        # Display status choices
        print("\nChoose new status:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Done")


        # Ask for new status
        status_choice = input(
            "Enter choice: "
        ).strip()


        # Change status
        if status_choice == "1":

            task["status"] = "PENDING"

        elif status_choice == "2":

            task["status"] = "IN PROGRESS"

        elif status_choice == "3":

            task["status"] = "DONE"

        else:

            print("\nInvalid status.")
            continue


        # Display confirmation
        print(
            f"\nTask #{task_id} status changed to "
            f"{task['status']}."
        )


    # --------------------------------------------------------
    # OPTION 5 - LIST ALL TASKS
    # --------------------------------------------------------

    elif choice == "5":

        # Check whether tasks exist
        if len(tasks) == 0:

            print("\nNo tasks available.")
            continue


        # Display heading
        print("\nALL TASKS")
        print("-" * 60)


        # Display every task
        for task in tasks:

            print(
                f"#{task['id']} | "
                f"{task['status']:<11} | "
                f"{task['priority']:<6} | "
                f"{task['title']}"
            )


        print("-" * 60)


    # --------------------------------------------------------
    # OPTION 6 - LIST DONE TASKS
    # --------------------------------------------------------

    elif choice == "6":

        # Create a list containing only completed tasks
        done_tasks = [
            task for task in tasks
            if task["status"] == "DONE"
        ]


        # Check whether any completed tasks exist
        if len(done_tasks) == 0:

            print("\nNo completed tasks.")

        else:

            print("\nDONE TASKS")
            print("-" * 60)


            # Display completed tasks
            for task in done_tasks:

                print(
                    f"#{task['id']} | "
                    f"{task['priority']:<6} | "
                    f"{task['title']}"
                )


            print("-" * 60)


    # --------------------------------------------------------
    # OPTION 7 - LIST PENDING TASKS
    # --------------------------------------------------------

    elif choice == "7":

        # Create a list containing pending tasks
        pending_tasks = [
            task for task in tasks
            if task["status"] == "PENDING"
        ]


        # Check whether pending tasks exist
        if len(pending_tasks) == 0:

            print("\nNo pending tasks.")

        else:

            print("\nPENDING TASKS")
            print("-" * 60)


            # Display pending tasks
            for task in pending_tasks:

                print(
                    f"#{task['id']} | "
                    f"{task['priority']:<6} | "
                    f"{task['title']}"
                )


            print("-" * 60)


    # --------------------------------------------------------
    # OPTION 8 - LIST IN-PROGRESS TASKS
    # --------------------------------------------------------

    elif choice == "8":

        # Create a list containing
        # only in-progress tasks
        progress_tasks = [
            task for task in tasks
            if task["status"] == "IN PROGRESS"
        ]


        # Check whether any exist
        if len(progress_tasks) == 0:

            print("\nNo in-progress tasks.")

        else:

            print("\nIN-PROGRESS TASKS")
            print("-" * 60)


            # Display in-progress tasks
            for task in progress_tasks:

                print(
                    f"#{task['id']} | "
                    f"{task['priority']:<6} | "
                    f"{task['title']}"
                )


            print("-" * 60)


    # --------------------------------------------------------
    # OPTION 9 - SEARCH TASKS
    # --------------------------------------------------------

    elif choice == "9":

        # Ask the user what they want to search
        search = input(
            "\nEnter text to search: "
        ).strip().lower()


        # Find tasks whose title contains
        # the search text
        matches = [
            task for task in tasks
            if search in task["title"].lower()
        ]


        # Check whether anything was found
        if len(matches) == 0:

            print("\nNo matching tasks.")

        else:

            print(
                f"\n{len(matches)} matching task(s):"
            )

            print("-" * 60)


            # Display matching tasks
            for task in matches:

                print(
                    f"#{task['id']} | "
                    f"{task['status']:<11} | "
                    f"{task['priority']:<6} | "
                    f"{task['title']}"
                )


            print("-" * 60)


    # --------------------------------------------------------
    # OPTION 10 - STATISTICS
    # --------------------------------------------------------

    elif choice == "10":

        # Count total tasks
        total = len(tasks)


        # Count tasks based on status
        done = len([
            task for task in tasks
            if task["status"] == "DONE"
        ])


        pending = len([
            task for task in tasks
            if task["status"] == "PENDING"
        ])


        progress = len([
            task for task in tasks
            if task["status"] == "IN PROGRESS"
        ])


        # Display statistics
        print("\nTASK STATISTICS")
        print("-" * 40)

        print(f"Total Tasks     : {total}")
        print(f"Pending         : {pending}")
        print(f"In Progress     : {progress}")
        print(f"Done            : {done}")


        # Calculate completion percentage
        if total > 0:

            percentage = done / total * 100

            print(
                f"Completion      : {percentage:.0f}%"
            )

        else:

            print("Completion      : 0%")


        print("-" * 40)