# sorting methods in list

marks = [78, 92, 67, 88, 85]

marks.sort()
print("Desc order = ", marks)

marks.sort(reverse=True)
print("Ascending = ", marks)

names = ["ravi", "Aisha", "karan", "Bhavna"]
print(sorted(names)) 
print(sorted(names, key=str.lower))

words = ["banana", "fig", "cherry", "kiwi"]
print(sorted(words, key=len))
print(sorted(words, key=len, reverse=True))

