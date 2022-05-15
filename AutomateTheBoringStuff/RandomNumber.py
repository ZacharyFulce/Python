import random
print('Hello, what is your name?')
name = input()
print('I am thinking of a number between 1 and 20.')

try:
    for guessesTaken in range(1,7):
        print('What is your guess?')
        guess = int(input())
        secretNumber = int(random.randint(1,20))
        if(guess > 0 and guess <= 20):
            if(guess < secretNumber):
                print(name + ', Your guess is too low. The actual number was ' + str(secretNumber) + '.')
            elif(guess == secretNumber):
                print(name + ', Your guess is correct. The actual number was ' + str(secretNumber) + '.')
            elif(guess > secretNumber):
                print(name + ', Your guess is too high. The actual number was ' + str(secretNumber) + '.')
        else:
            print('Invalid guess.')
except:
    print('Please enter a number between 1 and 20.')
