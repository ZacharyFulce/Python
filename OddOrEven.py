number = int(input('Please enter a number.'))
if(number % 2 == 0 and number % 4 == 0):
    print('Your number ' + str(number) + ' is a multiple of 4')
elif(number % 2 == 0):
    print('Your number ' + str(number) + ' is even.')
else:
    print('Your number ' + str(number) + ' is odd.')

num = int(input('Please enter a number.'))
check = int(input('Please enter another number.'))
if(num % check == 0):
    print('Your two numbers ' + str(num) + ', and ' + str(check) + ' are divisible by each other.')
else:
    print('Your two numbers ' + str(num) + ', and ' + str(check) + ' are not divisible by each other.')