num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
if num1>num2 and num1>num3:
    print("Frist number is greater than second and third.")
elif num2>num1 and num2>num3:
    print("Second number is greater than frist and third.")
else:
    print("Third number is greater than frist and second.")