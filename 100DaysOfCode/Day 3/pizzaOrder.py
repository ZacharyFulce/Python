from tkinter import E


size = input("Choose pizza size: small, medium, or large.\n")
bill = int(0)
try:
    if size == "Small" or size == "small":
        bill += 15
    elif size == "Medium" or size == "medium":
        bill += 20
    elif size == "Large" or size == "large":
        bill += 25
    except:
        print("Invalid Response")

pepperoni = input("Do you want pepperoni? Yes or No?\n")
if (size == "Small" or size == "small") and (pepperoni == "Yes" or pepperoni == "yes"):
    bill += 2
elif (size == "Medium" or size == "medium" or size == "Large" or size == "large") and (pepperoni == "Yes" or pepperoni == "yes"):
    bill += 3
elif pepperoni == "No" or pepperoni == "no":
    bill += 0
else:
    print("Please enter a valid response.")

cheese = input("Do you want extra cheese? Yes or No?\n")
if (size == "Small" or size == "small" or size == "Medium" or size == "medium" or size == "Large" or size == "large") and (cheese == "Yes" or cheese == "yes"):
    bill += 1
elif cheese == "No" or cheese == "no":
    bill += 0
else:
    print("Please enter a valid response.")

print(f"Your total order will be {bill}.")