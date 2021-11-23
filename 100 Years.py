print('What is your name?')
name = input()
print('What is your age?')
age = int(input())
if(age > 0 and age < 100):
    yearsLeft = 100 - age
    year = 2021 + yearsLeft
    print(name + ' will be 100 in ' + str(year))
else:
    print('Please enter a valid age')
