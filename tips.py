print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tipPercent = float(tip / 100)
split = int(input("How many people to split the bill? "))
billAmount = bill / split
tipAmount = (bill * tipPercent/split)
amountPerPerson = round((billAmount + tipAmount),2)
print(f"Each person should pay: ${amountPerPerson}")