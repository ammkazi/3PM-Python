vowels = "aeiou"
alphabets = "abcdefghijklmnopqrstuvwxyz"

text = input("Paste a paragraph: \n\n")

char_with_spaces = len(text)
char_no_spaces = len(text.replace(" ", ""))

words = text.split()

word_count = len(words)

sentences = text.count(".") + text.count("!") + text.count("?")

if sentences < 1:
    sentences = 1

vowel_count = 0
consonant_count = 0
digit_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count+=1
    elif ch in alphabets:
        consonant_count+=1
    elif ch.isdigit():
        digit_count+=1

total_letters = len("".join(words))

if word_count > 0:
    avg_word = total_letters / word_count
else:
    avg_word = 0

avg_sentence = word_count / sentences

if word_count > 0:
    longest = max(words, key=len)
else:
    longest = ""

if word_count > 0:
    shortest = min(words, key=len)
else:
    shortest = ""

print()

print("=" * 50)
print(f"{'VISUAL LABS TEXT ANALYSER':^50}")
print("=" * 50)

print(f"{'Characters (with spaces)':<32}{char_with_spaces:>16}")
print(f"{'Characters (no spaces)':<32}{char_no_spaces:>16}")

print(f"{'Words':<32}{word_count:>16}")

print(f"{'Sentences':<32}{sentences:>16}")

print(f"{'Vowels':<32}{vowel_count:>16}")

print(f"{'Consonants':<32}{consonant_count:>16}")

print(f"{'Digits':<32}{digit_count:>16}")

print(f"{'Average word length':<32}{avg_word:>16.2f}")

print(f"{'Average words per sentence':<32}{avg_sentence:>16.2f}")

print(f"{'Longest word':<32}{longest:>16}")

print(f"{'Shortest word':<32}{shortest:>16}")