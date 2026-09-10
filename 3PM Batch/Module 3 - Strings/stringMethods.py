text = "                            AN APPLE A DAY KEEPS DOCTOR AWAY               "
# print(text.lower())

address = "mumbai central"
# print(address.upper())

# print(text.casefold().strip())
# print(repr(text.casefold().rstrip()))

sentence = "##################The lazy fox jumps over the bush"
print(sentence.strip(" #"))

name = "sahil123"
print(name.rfind("S"))
print(name.count("Arkaan"))
# print(name.index("Z"))

print(name.isalpha()) # Only true when a letter is present
print(name.isdigit())
print(name.isalnum())

print(text.isupper())
print(text.islower())

interest = "I like programming in Python & Python"
# print(interest.replace("Python", "Java",1))
# print("a-b-c-d".replace("-", ""))

print(interest.find("z"))