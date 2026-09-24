squares = []
print(squares)

for sq in range(1,9):
    squares.append(sq*sq)
print(squares)
""
names = []
while True:
    entry = input("Name (blank to stop): ").strip()
    if not entry:
        break
    names.append(entry.title())

print(f"{len(names)} names collected: {names}")