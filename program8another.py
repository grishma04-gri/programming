gravity={1:0.38, 2:0.91, 3:0.38, 4:2.53, 5:1.07, 6:0.89, 7:1.14}
earth_weight=float(input("Enter your weight:"))
planet_number=int(input("Enter a planet number(1-7):"))
if planet_number in gravity:
    destination_weight=earth_weight*gravity[planet_number]
    print(f"Your weight on the selected planet:{destination_weight}")
else:
    print("Invalid planet number.")