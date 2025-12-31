units=int(input("Enter electricity usage(units):"))
if units<100:
    cost=units*5
elif units<=300:
    cost=units*5
    cost+=(units-100)*8
else:
    cost=100*5
    cost+=200*5
    cost+=(units-300)*100
print(f"Total electricity bill: Rs{cost}")
