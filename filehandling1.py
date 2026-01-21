#1
def extract_firstwords(filename):
    first_words_list = []
    with open("sample.txt", 'r') as file:
        for line in file:
            words = line.split()
            if words:
                first_words_list.append(words[0])
    return first_words_list
result = extract_firstwords('sample.txt')
print(result)

#2
def backup(filename1,filename2):
    with open('a.txt', 'r') as source_file, open('b.txt', 'w') as destination_file:
        for line in source_file:
            destination_file.write(line)
    return "File backup completed successfully."
print(backup("a.txt","b.txt"))

#3
def analyze_text_files(filename):
    with open("story.txt","r") as file:
        for line_number, line in enumerate(file, start=1):
            words=line.split()
            word_count=len(words)
            print(f"Line {line_number}: {word_count} words")
print(analyze_text_files("story.txt"))

#4
def linecount(filename):
    with open("story.txt","r") as file:
        line_count=0
        for line in file:
            line_count+=1
    return f"Total number of lines:{line_count}"
print(linecount("story.txt"))

#5
def filtering_line(filename1,filename2):
    with open('employees.txt', 'r') as source_file, open('management.txt', 'w') as dest_file:
        for line in source_file:
            if 'Python' in line:
                dest_file.write(line)
    return "Filtering complete. Lines containing 'Python' have been copied to management.txt."
print(filtering_line("employees.txt","management.txt"))

#6
def convert(filename1,filename2):
    with open('numbers.txt', 'r') as source, open('squared.txt', 'w') as destination:
        for line in source:
            if line.strip():
                number = int(line.strip())
                squared_number = number ** 2
                destination.write(str(squared_number) + '\n')
    return "Calculation complete. Results saved to squared.txt."
print(convert("numbers.txt","squared.txt"))

#7
def message(filename):
    user_message = input("Enter the message you want to log: ")
    with open('history.log', 'a') as file:
        file.write(user_message + '\n')
    return "Message successfully added to history.log."
print(message("history.log"))

#8
def cpaitalized(filename1,filename2):
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        for line in infile:
            capitalized_line = line.upper()
            outfile.write(capitalized_line)
    return "Conversion complete. All text in output.txt is now capitalized."
print(cpaitalized("input.txt","output.txt"))