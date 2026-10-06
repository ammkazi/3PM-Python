sentence = "apple banana apple orange banana apple mango orange banana apple"

counts = {}  # Create an empty dictionary to store word counts

for word in sentence.split():  # Take each word from the sentence
    counts[word] = counts.get(word, 0) + 1  # Increase its count by 1

for word in counts:  # Go through each word in the dictionary
    if counts[word] > 1:  # Check if the word appears more than once
        print(word, counts[word])  # Print the word and its count