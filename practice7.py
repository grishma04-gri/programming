a=int(input("Enter a number of students in class A:"))
b=int(input("Enter a number of students in class B:"))
c=int(input("Enter a number of students in class C:"))
desks_a=(a//2)+(a%2)
desks_b=(b//2)+(b%2)
desks_c=(c//2)+(c%2)
total_desks=desks_a+desks_b+desks_c
print(f"Minimun Numbers of desks needed:{total_desks}")
