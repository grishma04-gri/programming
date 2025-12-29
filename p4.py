num_items = int(input("How many items did you purchase? "))
prices = []
for i in range(num_items):
    price = float(input(f"Enter price of item {i + 1}: "))
    prices.append(price)
total_cost = sum(prices)
print(f"\nThe total cost of all {num_items} items is: ${total_cost:.2f}")