sentence = input("Enter a sentence: ")
words = sentence.split()
capitalised = []

for word in words:
    capitalised.append(word.capitalize())

print(" ".join(capitalised))
print(f"Words: {len(words)}")
print(f"Longest word: {max(words, key=len)}")
print(" ".join(reversed(words)))

print(" a b ".split())

# " ".join([1, 2, 3])

print(f"{0.5:.0%}")