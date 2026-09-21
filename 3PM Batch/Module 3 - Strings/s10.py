name = input("Enter fives names on a single line sepearted by comma: ")

words = name.split(",")
print(words)

for i, word in enumerate(words):
    print(i+1, word)