earth_weight=float(input("Enter your weight on Earth:"))
number=int(input("Enter a planet number(1-7):"))
if number==1:
    relative_gravity=0.38
elif number==2:
    relative_gravity=0.91
elif number==3:
    relative_gravity=0.38
elif number==4:
    relative_gravity=2.53
elif number==5:
    relative_gravity=1.07
elif number==6:
    relative_gravity=0.89
elif number==7:
    relative_gravity=1.14
else:
    print("Invalid planet number.")
    exit()
destination_weight=earth_weight*relative_gravity
print(f"Your weight on the selected planet:{destination_weight}")
