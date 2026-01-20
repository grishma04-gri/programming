# 1
items=["sql","123","Python"]
result=list(filter(lambda x:x.isalpha(),items))
print(result)

# 2
products=[{"id":1, "name":"Laptop","category":"electronics","price":1200,"instock":True},{"id":2, "name":"smartphone","category":"electronics","price":800,"instock":False}]
instock_products=list(filter(lambda p:p["instock"],products))
for product in instock_products:
    print(product)

# 3
def calculate_sum(start,end):
    total=0
    for i in range(start, end+1):
        total+=i
    return total
print(calculate_sum(1,5))

#4
def calculator():
    while True:
        print("\n----Simple Calculator-------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice=int(input("enter your choice(1-5):"))
        if choice==5:
            print("Calculator exited.")
            break
        elif choice in [1,2,3,4]:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            if choice==1:
                print(f"Result:{num1+num2}")
            elif choice==2:
                print(f"Result={num1-num2}")
            elif choice==3:
                print(f"Result:{num1*num2}")
            elif choice==4:
                if num2==0:
                    print("Error: Division by zero not allowed")
                else:
                    print(f"Result:{num1/num2}")
        else:
            print("Invalid choice. Try again.")
calculator()

#5
course=[{"Title":"Ancient Civilizations","Genre":"History"},{"Title":"Corporate Finance","Genre":"Commerce"},{"Title":"Modern World History","Genre":"History"}]
history_courses=list(filter(lambda c:c["Genre"]=="Hisotry",course))
for c in history_courses:
    print(c)

#6
emails=['ram.sharma@gmail.com','spam@hooya.com','virus@malware.net','shyam.kumar@workcorp.com']
blacklist=('@hooya.com','@malware.net')
spam_emails=list(filter(lambda email:email.endswith(blacklist),emails))
print(spam_emails)

#7
price=[100,50,200,75]
discounted_price=list(map(lambda p:p*0.8,price))
print(discounted_price)

#8
def skip_two(my_list):
    return my_list[1:12:3]
my_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(skip_two(my_list))

#9
def remove_at_idx(lst,idx):
    new_list=lst[:idx]+lst[idx+1:]
    return new_list
orginal=['a','b','c','d']
result=remove_at_idx(orginal,1)
print(result)

#10
text=input("Enter a string:")
cleaned="".join(ch if ch.isalnum() else "#" for ch in text)
print(f"Cleared string:{cleaned}")

#11
users_db={}
def register_user(username, password, email):
    if username in users_db:
        return "Username already exists"
    users_db[username]={
        "password":password,
        "email":email
    }
    return f"Registration successfull for {username}"
def login_user(username,password):
    if username not in users_db:
        return "User not found"
    if users_db[username]["password"]!=password:
        return "Incorrect password"
    return f"Welcome back {username}"
print(register_user('ram', 'ram123', 'ram@email.com'))
print(register_user('shyam', 'shyam456', 'shyam@email.com'))
print(register_user('hari', 'hari231', 'hari@email.com'))
print("\n---Login Tests---")
print(login_user('ram', 'ram123'))       
print(login_user('shyam', 'wrongpass'))  
print(login_user('unknown', '123'))

#12
def manage_inventory():
    inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]
    while True:
        print("\n--- Product Inventory Management ---")
        print("1. Add new product")
        print("2. View all products")
        print("3. Update product details")
        print("4. Delete a product")
        print("5. Calculate total inventory value")
        print("6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter product name: ").strip()
            if any(item['name'].lower() == name.lower() for item in inventory):
                print(f"Error: Product '{name}' already exists.")
                continue
            try:
                price = float(input("Enter price: "))
                qty = int(input("Enter quantity: "))
                if price <= 0 or qty <= 0:
                    print("Error: Price and Quantity must be positive numbers.")
                    continue
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
                continue
            inventory.append({'name': name, 'price': price, 'quantity': qty})
            print(f"Success: {name} added to inventory.")
        elif choice == '2':
            if not inventory:
                print("Inventory is empty.")
            else:
                print(f"\n{'Name':<20} | {'Price':<10} | {'Quantity':<10}")
                print("-" * 45)
                for item in inventory:
                    print(f"{item['name']:<20} | {item['price']:<10.2f} | {item['quantity']:<10}")
        elif choice == '3':
            name = input("Enter the name of the product to update: ").strip()
            found = False
            for item in inventory:
                if item['name'].lower() == name.lower():
                    try:
                        new_price = float(input(f"Enter new price for {item['name']}: "))
                        new_qty = int(input(f"Enter new quantity for {item['name']}: "))
                        if new_price <= 0 or new_qty <= 0:
                            print("Error: Values must be positive.")
                        else:
                            item['price'] = new_price
                            item['quantity'] = new_qty
                            print(f"Success: {item['name']} updated.")
                        found = True
                        break
                    except ValueError:
                        print("Error: Invalid input.")
                        found = True # Break loop but skip update
                        break
            if not found:
                print("Error: Product not found.")
        elif choice == '4':
            name = input("Enter the name of the product to delete: ").strip()
            original_len = len(inventory)
            inventory = [item for item in inventory if item['name'].lower() != name.lower()]
            
            if len(inventory) < original_len:
                print(f"Success: Product '{name}' deleted.")
            else:
                print("Error: Product not found")
        elif choice == '5':
            total_value = sum(item['price'] * item['quantity'] for item in inventory)
            print(f"Total Inventory Value: {total_value:,.2f}")
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
if __name__ == "__main__":
    manage_inventory()

#13
def validate_phone(phone):
    """Checks if phone is exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    """Checks if email contains @ and ."""
    return "@" in email and "." in email

def main():
    contacts = [{'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}]
    while True:
        print("\n--- CONTACT MANAGEMENT SYSTEM ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact by Name")
        print("4. Update Contact Information")
        print("5. Delete Contact")
        print("6. Sort Contacts Alphabetically")
        print("7. Exit")       
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            name = input("Enter Name: ").strip()
            if any(contact['name'].lower() == name.lower() for contact in contacts):
                print("Error: A contact with this name already exists.")
                continue
            phone = input("Enter Phone (10 digits): ")
            if not validate_phone(phone):
                print("Invalid phone format! Must be 10 digits.")
                continue
            email = input("Enter Email: ")
            if not validate_email(email):
                print("Invalid email format! Must contain '@' and '.'.")
                continue
            contacts.append({'name': name, 'phone': phone, 'email': email})
            print("Contact added successfully!")
        elif choice == '2':
            if not contacts:
                print("Contact list is empty.")
            else:
                print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25}")
                print("-" * 60)
                for c in contacts:
                    print(f"{c['name']:<20} | {c['phone']:<15} | {c['email']:<25}")
        elif choice == '3':
            search_name = input("Enter name to search: ").lower()
            found = False
            for c in contacts:
                if c['name'].lower() == search_name:
                    print(f"Found: Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
                    found = True
                    break
            if not found:
                print("Contact not found.")
        elif choice == '4':
            update_name = input("Enter the name of the contact to update: ").lower()
            for c in contacts:
                if c['name'].lower() == update_name:
                    print(f"Updating record for {c['name']}")
                    
                    new_phone = input("Enter new phone (leave blank to keep current): ")
                    if new_phone:
                        if validate_phone(new_phone):
                            c['phone'] = new_phone
                        else:
                            print("Invalid format. Phone not updated.")                   
                    new_email = input("Enter new email (leave blank to keep current): ")
                    if new_email:
                        if validate_email(new_email):
                            c['email'] = new_email
                        else:
                            print("Invalid format. Email not updated.")
                    print("Update process complete.")
                    break
            else:
                print("Contact not found.")
        elif choice == '5':
            del_name = input("Enter the name to delete: ").lower()
            original_len = len(contacts)
            contacts = [c for c in contacts if c['name'].lower() != del_name]            
            if len(contacts) < original_len:
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        elif choice == '6':
            contacts.sort(key=lambda x: x['name'].lower())
            print("Contacts sorted alphabetically.")
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()