age=int(input("Enter your age:"))
if age>=18 and age<30:
    gender=input("Enter your gender(M/F):").lower()
    if gender=="m":
        print("Your wage per day: Rs.700")
    elif gender=="f":
        print("Your wage per day: Rs.750")
    else:
        print("not in option.")
elif age>=30 and age<=40:
    gender=input("Enter your gender (F/M):").lower()
    if gender=="f":
        print("Your wage per day: Rs.850")
    elif gender=="m":
        print("Your wage per day: Rs.800")
    else:
        print("Not in option.")
else:
    print("Invalid Age.")