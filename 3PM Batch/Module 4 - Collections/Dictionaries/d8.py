students = [
    {"name": "Aisha", "roll": 1, "marks": {"maths": 92, "science": 88}},
    {"name": "Ravi", "roll": 2, "marks": {"maths": 78, "science": 71}},
    {"name": "Karan", "roll": 3, "marks": {"maths": 85, "science": 95}},
]

print(students[0]["name"])
print(students[0]["marks"]["maths"])

print(f"\n{'ROLL':<6}{'NAME':<10}{'MATHS':>7}{'SCIENCE':>9}{'TOTAL':>7}")
print("-" * 39)

for s in students:
    total = sum(s["marks"].values())
    print(f"{s['roll']:<6}{s['name']:<10}"
          f"{s['marks']['maths']:>7}{s['marks']['science']:>9}{total:>7}")

topper = max(students, key=lambda s: sum(s["marks"].values()))
print(f"\nTopper: {topper['name']}")