class Student:
    name = "sahil"
    roll_no = "002"

    def display(self):
        print("Student name: ", self.name)
        print("Student roll number: ", self.roll_no)

s1 = Student()
s2 = Student()
s3 = Student()

s2.name = "Kaif"
s2.roll_no = "003"

s3.name = "Zeeshan"
s3.roll_no = "004"

s1.display()
s2.display()
s3.display()