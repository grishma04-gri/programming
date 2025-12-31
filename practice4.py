age=int(input("Enter your age:"))
if age<12:
    price=0
else:
    membership=input("Do you have a membership card(y/n):").lower()
    if age>=12 and age<=60:
        if membership=="y":
            price=150
        else:
            price=200
    else:
        price=100
print(f"Your movie ticket price:Rs{price}")