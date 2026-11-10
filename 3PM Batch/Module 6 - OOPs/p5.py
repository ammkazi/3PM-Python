

class Employee:

    company = "Vijay Sales" # Class Attribute
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary # Instance Method Variables
        

    def display(self):
        print("Employee name : " , self.name)
        print("Employee ID : " , self.id)
        print("Salary : " , self.salary)
        print("Company : " , self.company)


em1 = Employee("Aiman", 101,1230)
em1.company = "Ashok INstitute"

em2 = Employee("Kaif", 102, 5000)


em3 = Employee("Sahil", 103, 5000)

print(em1.company)
print(em2.company)
print(em3.company)

