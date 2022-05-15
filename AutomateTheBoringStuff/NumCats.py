print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats! You have ' + numCats + ' cats.')
    elif int(numCats)> 0 and int(numCats) <4:
        print('That is not that many cats. You only have ' + numCats + ' cats.')
    else:
        print('You do not have any cats.')
except ValueError:
    print('You did not enter a number.')