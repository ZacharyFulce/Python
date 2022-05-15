age = int(input("Please enter your age in years\n"))
ageInDays = age * 365
ageInWeeks = age * 52
ageInMonths = age * 12
daysLeft = (90 * 365 - ageInDays)
weeksLeft = (90 * 52 - ageInWeeks)
monthsLeft = (90 * 12 - ageInMonths)
print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")