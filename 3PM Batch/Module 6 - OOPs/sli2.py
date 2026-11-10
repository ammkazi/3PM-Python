class Employee:
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

    def display_employee(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.id)
        print("Department:", self.dept)

class Manager(Employee):
    def __init__(self, name, emp_id, dept, team_size):
        # FIXED: Changed 'id' to 'emp_id' to match the parameter above
        super().__init__(name, emp_id, dept) 
        self.team_size = team_size

    def display_manager(self):
        self.display_employee()
        print("Team Size:", self.team_size)

# Running the code
m1 = Manager("Rakesh", 101, "Sales", 10)
m1.display_manager()
