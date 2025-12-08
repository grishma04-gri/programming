shopping_list={"Milk","Bread","Eggs"}
brought_contaning={"Bread","Eggs"}
remaining=shopping_list-brought_contaning
if remaining:
    print(f"Still need to buy: {remaining}")
else:
    print("Shopping Completed!")