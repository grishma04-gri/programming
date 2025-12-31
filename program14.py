print("**** Welcome to Magic Forest ****")
want_to_go=input("Enter where you want to go(North/South):").lower()
if want_to_go=="south":
    print("Game Over!")
elif want_to_go=="north":
    want_to=input("Enter whether you want to 'cross the river' or 'follow the path':").lower()
    if want_to=="cross the river":
        print("Game Over!")
    elif want_to=="follow the path":
        choose=input("Choose between 'fairy', 'ogre' or 'elf':").lower()
        if choose=='fairy'or choose=='orge':
            print("Game Over!")
        elif choose=='elf':
            print("You win!")
        else:
            print("Invalid Choice!")
    else:
        print("Invalid Choice!")
else:
    print("Invalid Choice!")