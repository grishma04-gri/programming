contacts={
    "Grishma Pokharel":"grishma.pokharel@example.com",
    "Anjana Sharma":"anjana.sharma@gmail.com",
    "Shreeya Timilsina":"shreeya.timilsina@example.com"
}
name=input("Enter your name:")
if name in contacts:
    print(f"Email: {contacts[name]}")
else:
    print("Contacts not found.")
