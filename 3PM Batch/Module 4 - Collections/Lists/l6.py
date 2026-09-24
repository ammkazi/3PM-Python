list = []
ask = int(input("How many names do u want to enter?: "))

for i in range(ask):
    name = input("Enter name: ")
    list.append(name)

print(list)

for l in list:
    if len(l) > 5:
        print("Name longer than 5 chars is: ",l)