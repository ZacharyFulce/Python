height = float(input("Please enter your height in meters\n"))
h2 = height ** 2
weight = float(input("Please enter your weight in kilograms\n"))
bmi = round(weight / h2)
if bmi < 18.5:
    result = "you are underweight."
elif bmi >= 18.5 and bmi < 25:
    result = "you are normal weight."
elif bmi >= 25 and bmi <= 30:
    result = "you are overweight."
elif bmi >= 30 and bmi <= 35:
    result = "you are obese."
else:
    result = "you are clinicially obese."
print(
    f"Your weight is {weight} kilograms, and your height is {height} meters. Your BMI is {bmi} and {result}")
