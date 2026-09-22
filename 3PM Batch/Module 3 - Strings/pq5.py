# Store the total salary paid to all employees
total_salary = 0

# Process 10 employees
for employee in range(1, 5):

    # Display the employee number
    print("\nEmployee", employee)

    # Ask for the Employee ID
    employee_id = input("Enter Employee ID: ")

    # Ask for the number of days the employee was present
    days_present = int(input("Enter days present: "))

    # Ask for the number of overtime hours
    overtime_hours = float(input("Enter overtime hours: "))

    # If attendance is 0, skip salary calculation
    if days_present == 0:
        print("No salary calculation for", employee_id)
        continue

    # Check if attendance is below 18 days
    if days_present < 18:

        # Display the low attendance warning
        print("Warning: Low Attendance")

        # Employee gets 50% of the basic salary
        attendance_salary = 25000 * 0.50

    # Check if attendance is between 18 and 21 days
    elif days_present < 22:

        # Employee gets 75% of the basic salary
        attendance_salary = 25000 * 0.75

    # Check if attendance is between 22 and 25 days
    elif days_present < 26:

        # Employee gets 90% of the basic salary
        attendance_salary = 25000 * 0.90

    # If attendance is 26 days or more
    else:

        # Employee gets 100% of the basic salary
        attendance_salary = 25000

    # Calculate overtime salary
    overtime_salary = overtime_hours * 300

    # Calculate the employee's total salary
    salary = attendance_salary + overtime_salary

    # Add this employee's salary to the company total
    total_salary += salary

    # Display the employee's salary
    print("Employee Salary: Rs.", salary)


# Display the total salary paid by the company
print("\nTotal Salary Paid by Company: Rs.", total_salary)