# FIND THE PERCENTAGE DIFFERENCE BETWEEN TWO NUMBERS

import os
import subprocess

def display():
    os.system('clear')
    # os.system('figlet -f mini "% C H A N G E"')
    print('PERCENTAGE CHANGE')
    print('\n')


def percent_diff():
    x = float(input("Enter starting number: "))
    y = float(input("Enter ending number: "))
    print('\n')

    diff = y - x
    answer = diff / x * 100

    return "%.2f" % answer


display()
print(f'CHANGE: {percent_diff()}%')


