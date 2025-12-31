is_valid=True
balance=5000
correct_pin=123
if is_valid:
    pin=int(input("Enter your PIN:"))
    if pin==correct_pin:
        print("\n--- ATM Menu ---")
        print("1. Withdraw")
        print("2. Check Balance.")
        print("3. Exit")
        choice=int(input("Enter your choice(1-3):"))
        if choice==1:
            amt=float(input("Enter amount to withdraw:"))
            if amt<=balance:
                balance-=amt
                print("Withdrawl successfull!")
                print(f"Remaining balance:{balance}")
                print("Thank you for visiting!")
            else:
                print("Insufficient Balance! Try Again.")
        elif choice==2:
            print(f"Your Current Balance:{balance}")
            print("Thank you for visiting!")
        elif choice==3:
            print("Thank you for visitng! Exit")
        else:
            print("Invalid Choice.")
    else:
        print("Wrong PIN! Access Denied.")
else:
    print("Invalid Card!")
    