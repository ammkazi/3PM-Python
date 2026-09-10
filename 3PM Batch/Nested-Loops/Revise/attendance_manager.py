students = []
days = ["Monday", "Tuesday", "Wednesday","Thursday","Friday"]

print(days)

for i in range(0,3):
    student= input("Enter student name: ")
    students.append(student)

for student in students:
    present = 0

    print(f"\nAttendance for {student}")

    for day in days:
        status = input(f"{day} (P/A): ")
        if status == "P" or status == "p":
            present += 1
        elif status == "A" or status == "a":
            pass
        else:
            print("Invalid input!!")

    print("Days present: ", present)

    if present == 5:
        print("Pefect Attendance!")
    elif present >= 3:
        print("Good")
    elif present >= 1:
        print("Poor")
    else:
        print("Absent All Week")
    