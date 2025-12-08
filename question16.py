student = {
    "name": "Hari",
    "course": "Robotics",
    "grade": 9
}
valid_courses = ["Creative Writing", "Robotics", "Digital Art"]
name = student["name"]
course = student["course"]
grade = student["grade"]
if course not in valid_courses:
    print(f"{name} selected an invalid course.")
elif grade < 9 or grade > 12:
    print(f"{name} is not eligible for {course} (grade too low).")
elif course == "Robotics" and grade == 9:
    print(f"{name} is not eligible for {course} (grade too low).")
else:
    print(f"{name} is approved for {course}.")
