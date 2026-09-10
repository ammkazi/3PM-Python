word = input("Enter a string to check vowels: ")
vowels = "AEIOUaeiou"

for w in word:
    if w in vowels:
        print(w)