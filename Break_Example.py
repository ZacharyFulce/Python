name = ''
'''
while name != 'Your name':
    print('Please type your name')
    name = input()
'''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')