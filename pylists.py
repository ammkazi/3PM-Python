# list , tuple, set and dictionary

#List -> [ ]
list1= ["Fruits", "milk", "egg", 12 , 10.4, True]
print(type(list1))

# # index position -> 0 - (n-1)
print(list1[2])
print(list1[5])

# #Negative indexing -> Access elements in reverse order
print(list1[-5])

# # Lists are mutable
list1[3] = "Burberry"

list1[4] = 100.4
print(list1)

# #List methods:-
list1.append("Amazon")
print(list1)

list1.insert(1, "Samsung")
print(list1)

list2 = ["Mavia", 23, "Maths", 23]
list1.extend(list2)
print(list1)
print(list2)

list2.remove(23)
print(list2)

list2.pop(2)
print(list2)

list2.clear()
print(list2)