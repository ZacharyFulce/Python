import random
myList = ['rock', 'paper', 'scissors']
print('Let"s play rock, paper, scissors')

try:
    for a in range(0, 4):
        print('Rock, paper, or scissors?')
        choice = (input())
        choice.lower()
        cpu = random.choice(myList)

        if(choice == 'rock' and cpu == 'rock' or choice == 'paper' and cpu == 'paper' or choice == 'scissors' and cpu == 'scissors'):
            print('You and the computer both chose ' + str(choice) + '.')

        elif(choice == 'rock' and cpu == 'scissors' or choice == 'paper' and cpu == 'rock' or choice == 'scissors' and cpu == 'paper'):
            print('You have won! You chose ' + str(choice) +
                  ' and the CPU chose ' + str(cpu) + '.')

        elif(choice == 'rock' and cpu == 'paper' or choice == 'paper' and cpu == 'scissors' or choice == 'scissors' and cpu == 'rock'):
            print('You have lost! You chose ' + str(choice) +
                  ' and the CPU chose ' + str(cpu) + '.')

    '''
    print('You have won ' + str(won) + ' game(s), lost ' + str(lost) +
            ' game(s) and tied ' + str(tie) + ' game(s) so far.')
    '''

except:
    print('Please choose "Rock", "Paper", or "Scissors".')
