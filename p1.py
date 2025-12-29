word=input("Enter any word or sentence:")
vowels=set()
for ch in word:
    if ch in "AEIOUaeiou":
        vowels.add(ch)
print(f"Vowels: {vowels}")
