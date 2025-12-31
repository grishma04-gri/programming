cost_price=float(input("Enter a cost price of bike:"))
if cost_price>100000:
    tax_rate=0.15 #15%
elif cost_price>50000 and cost_price<=100000:
    tax_rate=0.10 #10%
else:
    tax_rate=0.05 #5%
tax_amount=cost_price*tax_rate
print(f"Road tax to be paid:Rs.{tax_amount}")