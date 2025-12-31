m1=float(input("Enter marks of subject1:"))
m2=float(input("Enter marks of subject2:"))
m3=float(input("Enter marks of subject3:"))
m4=float(input("Enter marks of subject4:"))
total=m1+m2+m3+m4
percentage=total/4
if percentage>70:
    grade="Distinction"
elif percentage>60:
    grade="Frist Division"
elif percentage>40:
    grade="Pass"
else:
    grade="Fail"
print(f"Total marks:{total}")
print(f"Percentage:{percentage}")
print(f"Grade:{grade}")