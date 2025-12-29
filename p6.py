sentence = input("Enter a sentence: ")
words = sentence.split()
word_counts = {}
for word in words:
    clean_word = word.lower()
    word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
print("\nWord Frequencies (Alphabetical Order):")
for word in sorted(word_counts.keys()):
    print(f"{word}: {word_counts[word]}")