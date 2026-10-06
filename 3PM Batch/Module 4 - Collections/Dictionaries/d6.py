marks = {"Maths": 92, "Physics": 78, "Chemistry": 85}

# Create a dictionary to store percentages
percentages = {}

for sub in marks:
    percentages[sub] = str(marks[sub]) + "%"

# Create a dictionary for subjects where marks are 80 or above
passed = {}

for sub in marks:
    if marks[sub] >= 80:
        passed[sub] = marks[sub]

# Create a dictionary with marks as keys and subjects as values
inverted = {}

for sub in marks:
    inverted[marks[sub]] = sub # inverted[92] = maths

print(percentages)
print(passed)
print(inverted)