student={
    "name":input("Enter your name:").lower(),
    "course":input("Enter your course:").lower(),
    "grade":int(input("Enter grade:"))
    }
valid_course={"maths","physics","computer science"}
min_grade={"maths":70,
           "physics":60,
           "computer science":75
        }
name=student["name"]
course=student["course"]
grade=student["grade"]
if course not in valid_course:
    print("Invalid Course")
elif grade<min_grade[course]:
    print(f"Grade too low for {course}.")
else:
    print(f"{name} approved for {course}.")