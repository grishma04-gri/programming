num=int(input("enter a number:"))
if num>0:
    print("Number is positive.")
    if (num%2)==0:
        print("number is even.")
    else:
        print("number is odd.")
elif num<0:
    print("number is negative.")
else:
    print("number is zero.")
    