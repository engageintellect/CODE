import os
import time

os.system('clear')

guesses = 5

for x in range(5):
    print('\n')
    a = input('enter a number: ')
    print('you entered ' + a)
    guesses = guesses -1
    print('you have ' + str(guesses) + ' guesses remaining...')
    time.sleep(2)
    os.system('clear')

