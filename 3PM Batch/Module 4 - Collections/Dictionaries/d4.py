marks = {"Maths": 92, "Physics": 78, "Chemistry": 85, "Biology": 67}

for subject in marks:
    print(subject, end=" ")
print("\n")

for subject, score in marks.items():
    print(f"{subject:<12}{score:>5}")

print("Keys in dictionary: ", list(marks.keys()))
print("Values in dictionary: ", list(marks.values()))
print(f"Total {sum(marks.values())}, average {sum(marks.values()) / len(marks):.2f}")
print(f"Topper: {max(marks, key=marks.get)}")