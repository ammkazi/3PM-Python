list = ["Mango" , "Banana", "Apple", "Dragonfruit"]
print(list)

student = ["Zeeshan", 32, 3.14, True]
print(student)

student[2] = "Dhorajiwala"
print(student)

#Adding elements
student.append("BMW")
print(student)

student.insert(2, "Mango")
print(student)


student.extend(["abizer", "abu dhabi"])
print(student)


#Removing Elements
student.pop(3)
print(student)

student.remove("BMW")
print(student)


print(student)

# student.clear()
# print(student)

# del student
# print(student)

print(len(list))
print(len(student))

print( student + list ) # list concatenation

print(student * 7)