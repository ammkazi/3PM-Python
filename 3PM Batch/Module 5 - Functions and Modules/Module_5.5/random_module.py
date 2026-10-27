import random

# for i in range(10):
#     num = random.randint(1,10)
#     print(num)


# list = ["Arkaan", "Sahil", "Aiman", "Kaif", "Zeeshan"]
# print(random.choice(list))
# random.shuffle(list)

# print(list)


students = ["Aman", "Sara", "Rahul", "Priya", "Zoya"]

selected = random.sample(students, 5)

print("Selected students:", selected)