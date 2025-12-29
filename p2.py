word_dict={}
n=int(input("Enter a number of operations:"))
for n in range(1,n+1):
    print("\nMenu")
    print("1. Add a word")
    print("2. Display all words")
    print("3. Remove a word")
    print("4. Exit")
    choice=int(input("Enter your choice(1-4):"))
    if choice==1:
        word=input("Enter word:")
        if word in word_dict:
            print("Word already exists.")
        else:
            meaning=input("Enter meaning:")
            word_dict[word]=meaning
            print("Word added successfully.")
    elif choice==2:
        if not word_dict:
            print("Dictionary is empty.")
        else:
            for word in sorted(word_dict):
                print(f"Word: {word}, Meaning: {word_dict[word]}")
    elif choice==3:
        word=input("Enter word to remove.")
        if word in word_dict:
            del word_dict[word]
            print("Word removed successfully.")
        else:
            print("Word not found.")
    elif choice==4:
        print("Existing program.")
        break
    else:
        print("Invalid choice.")