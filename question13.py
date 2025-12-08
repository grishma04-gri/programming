class_list=["ram","sita","laxman"]
new_student="ram"
if new_student not in class_list:
    class_list.append(new_student)
    print(f"Added {new_student}")
else:
    print(f"{new_student} is alreay in class.")