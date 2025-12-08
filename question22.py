alice_items = {"apple", "banana", "orange"}
bob_items = {"milk", "bread", "apple"}
if alice_items.isdisjoint(bob_items):
    print("They picked completely different items.")
else:
    print("They have some common items.")
