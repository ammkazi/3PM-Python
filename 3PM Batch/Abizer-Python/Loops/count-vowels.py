vowels = "AEIOUaeiou"
word = input("Enter a word: ")
count = 0

for w in word:
    if w in vowels:
        count+=1
        print(w)

print("There are total ", count,"vowels")