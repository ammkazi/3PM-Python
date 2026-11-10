class Employee:

    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary


    def displayEmployee(self):
        print("=" * 40)
        print("Employee Name : " + self.name)
        print("Employee ID : " , self.id)
        print("Employee Salary : ", self.salary)
        print("="*40)


emp1 = Employee("Kaif", 101, 60000)
emp2 = Employee("Sahil", 102, 90000)

emp1.displayEmployee()
emp2.displayEmployee()

em3 = Employee("Zeeshan", 103, 9000)
em3.displayEmployee()


        