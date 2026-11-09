# Constructors

class Student:

    def __init__(self, name, roll_no):
        print("Student object created") #Constructor
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

s1 = Student("Kaif", "101")
s1.display()

s2 = Student("Sahil", "102")
s2.display()