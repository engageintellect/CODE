import os
import time

hint = "its round."

os.system('clear')
words = ['kalani']
guesses = 5

for x in range(5):
    print("HINT: " + hint + ".")

    print('\n')
    a = input('guess word: ')
    os.system('clear')
    time.sleep(1)
    print('\n')
    print('you entered ' + a)
    time.sleep(2)
    os.system('clear')

    if a in words:
        print('\n')
        print('CORRECT!')
        time.sleep(2)
        os.system('clear')
        quit()
    else:
        print('\n')
        print('WRONG!')
        print('\n')
        guesses = guesses -1
        print('you have ' + str(guesses) + ' guesses remaining...')
        time.sleep(2)
        os.system('clear')

