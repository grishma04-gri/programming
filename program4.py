num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
if num1>num2:
    print("Frist number is greater than second.")
elif num2>num1:
    print("Second number is greater than frist.")
else:
    print("Both the numbers are equal.")
    if num1>0 and num2>0:
        print("Positve number.")
    elif num1<0 and num2<0:
        print("Negative number.")
    else:
        print("Given number is zero.")
        