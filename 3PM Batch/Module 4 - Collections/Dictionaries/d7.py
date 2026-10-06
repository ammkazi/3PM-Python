marks = {"Maths": 92, "Physics": 78, "Chemistry": 85}

percentages = {sub: f"{score}%" for sub, score in marks.items()}

passed = {sub: score for sub, score in marks.items() if score >= 80}

inverted = {score: sub for sub, score in marks.items()}

print(percentages)
print(passed)
print(inverted)