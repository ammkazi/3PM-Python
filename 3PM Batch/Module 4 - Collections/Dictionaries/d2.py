student = {"name": "Aisha", "roll": 21}

student["course"] = "Python"
student.update({"city": "Bangalore", "marks": 92})
print(student)

pop_value = student.pop("city")
print(pop_value)

print(student)

del student["marks"]
print(student)
del student
print(student)
