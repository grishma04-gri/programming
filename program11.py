service_timeperiod=float(input("Enter a time period of service:"))
salary=float(input("Enter employee salary:"))
if service_timeperiod>10:
    bonus_rate=0.10 #10%
elif service_timeperiod>=6 and service_timeperiod<=10:
    bonus_rate=0.08 #8%
else:
    bonus_rate=0.05 #5%
bonus_amount=salary*bonus_rate
print(f"Bonus amount: Rs.{bonus_amount}")
