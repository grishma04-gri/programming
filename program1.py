num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if num1==num2 and num2==num3 and num1==num3:
    print("All number are equal.")
elif num1==num2 or num2==num3 or num1==num3:
    print("Two numbers are equal.")
else:
    print("All numbers are different.")