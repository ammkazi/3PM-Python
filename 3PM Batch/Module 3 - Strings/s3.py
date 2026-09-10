vowels = 0
name = "Visual Labs"

for v in name.lower():
    if v in "aeiou":
        print(v + " is a vowel")
        vowels += 1
print("Total ", vowels , "vowels")

print("cat" in "concatenate")