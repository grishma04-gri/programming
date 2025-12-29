sentence = input("Please enter a full sentence: ")
word_list = sentence.split()
total_words = len(word_list)
unique_words = set()
for word in word_list:
    unique_words.add(word.lower())
print(f"\nTotal number of words typed: {total_words}")
print(f"Number of unique words used: {len(unique_words)}")