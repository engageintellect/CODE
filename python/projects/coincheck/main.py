#!/usr/bin/env python3


import subprocess
import os


def display():
    os.system('clear')
    os.system('figlet coincheck')
    print('\n')


def main():
    display()
    ticker = str(input("Input ticker: "))
    
    while ticker != 'q':
        timeframe = str(input("Choose timeframe: "))
        os.system('clear')
        output = subprocess.getoutput(f'curl -s rate.sx/{ticker}@{timeframe}')
        print(output)
        usr_continue = input("PRESS ENTER TO CONTINUE > ")
        if usr_continue == '':
            pass
        else:
            os.system('clear')
            quit()
        main()
    else:
        os.system('clear')
        quit()



main()
