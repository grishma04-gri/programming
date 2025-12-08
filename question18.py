banned_items={"scissors","knife","lighter"}
weight=float(input("Enter your  baggsge weight:"))
iteams=input("Enter the iteam you are carring:").lower()
if weight<=7 and iteams not in banned_items:
    print("Bag accepted.")
else:
    print("Bag not allowed.")