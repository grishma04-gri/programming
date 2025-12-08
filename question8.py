i=int(input("Enter a number for i:"))
j=int(input("Enter a number for j:"))
k=int(input("Enter a number for k:"))
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print(i,j,k)