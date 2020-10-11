# NUMBER GUESSING GAME

# IMPORTS
from random import randrange
import time
import os

# CLEAR DISPLAY
os.system('clear')

# GENERATE RANDOM NUMBER BETWEEN 0-100
num = (randrange(101))

# DISPLAY
def display():
    print('GUESS A NUMBER BETWEEN 0-100: ')

# USER INPUT
def guess_num():
    display()
    guess = input(': ')

    # IF GUESS IS CORRECT
    if int(guess) == int(num):
        os.system('clear')
        print('CORRECT!!!')
        time.sleep(1)
        print('The number was ' + str(num))

    # IF GUESS IS WRONG
    else:
        if int(guess) > int(num):
            print('TOO HIGH')
            time.sleep(1)
            os.system('clear')
            guess_num()
        if int(guess) < int(num):
            print('TOO LOW')
            time.sleep(1)
            os.system('clear')
            guess_num()


# RUN MAIN
guess_num()
