skills = {"python", "sql"}

skills.add("java")
print(skills)

skills.update(["html", "css"])
print(sorted(skills))

skills.discard("java")
print(sorted(skills))

print("python" in skills)