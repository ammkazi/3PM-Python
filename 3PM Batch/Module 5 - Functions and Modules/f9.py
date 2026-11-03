# def greet(name = "John Doe"): # Default parameter
#     print("Name : ", name)

# greet("Kaif Sange")

def greet(name,text = "Hello", punc="!"):
    print(f"{text} {name} {punc}")

greet("Kaif", "Hi")
greet("Arkaan")

