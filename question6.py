i=int(input("Enter a number of i:"))
j=int(input("Enter a number of j:"))
k=int(input("Enter a number of k:"))
if i<10:
    if j>5:
        print("Result A")
    else:
        if k%2==0:
            print("Result B")
        else:
            print("Result C")
else:
    if k>10:
        if i==k:
            print("Result D")
        else:
            print("Result E")
    else:
        print("Result F")