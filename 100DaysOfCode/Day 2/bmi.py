height = float(input("Please enter your height in meters\n"))
h2 = height ** 2
weight = float(input("Please enter your weight in kilograms\n"))
bmi = weight / h2
print("Your weight is " + str(weight) + " kilograms, and your height is " + str(height) + " meters. Your BMI is " + str(bmi))