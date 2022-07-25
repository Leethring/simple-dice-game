#! python3
# throwDiceGame.py - A simple word dice game 

import random

print('There is a dice in front of you. Type any key to start a dice game.')
print('(Type q to exit)\n')
startAGame = input()
while startAGame != 'q':
    print('Please type Enter to throw a dice to get a number between 1-6:')
    print('If you do not want to play this game, type q to exit this game.')
    x = input()
    print('')
    while x != "":
        if x == 'q':
            break
        print('You typed wrong key. Please type Enter.')
        print('If you do not want to play this game, type q to exit this game.')
        x = input()
        print('')
    if x == 'q':
        break
    randomNumber = random.randint(1,6)
    print('Your dice number is ' + str(randomNumber))
    print('')
print('You have terminated this dice game.\n')
