amount=int(input("Enter total purchase:"))
customer=input("is Member (True/False):").lower()
if amount>1000 and customer=='true':
    print("Discount is 20%")
    final_amount=amount-0.2*amount
    print(f"Total amount={final_amount}")
elif amount>1000 and customer=="false":
    print("Discount is 10%")
    final_amount=amount-0.1*amount
    print(f"Total amount={final_amount}")
else:
    print("No Discount")
    print(f"Total amount={amount}")