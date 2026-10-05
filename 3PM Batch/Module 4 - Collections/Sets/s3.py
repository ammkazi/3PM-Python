# Set Operations
python_students = {"Aisha", "Ravi", "Karan", "Neha"}
sql_students = {"Ravi", "Neha", "Farah"}

print(python_students.union(sql_students)) # ( either use | or union() function)
print(python_students.intersection(sql_students)) # either use & or intersection() function)
print(python_students.difference(sql_students)) # either use - or difference()
print(python_students.symmetric_difference(sql_students))