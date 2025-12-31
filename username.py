correct_username='admin1'
correct_password="adm1234"
username=input("enter a username:")
if username==correct_username:
    password=input("enter a password:")
    if password==correct_username:
        print("Login Successful! Welcome.")
    else:
        print("Incorrect Password.")
else:
    print("Incorrect Username.")
