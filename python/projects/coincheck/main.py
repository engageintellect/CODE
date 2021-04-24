#!/usr/bin/env python3


import subprocess
import os



def main():

    os.system('clear')
    os.system('figlet coincheck')
    print('\n')
    
    ticker = str(input("Input ticker: "))
    if ticker != 'q':
        timeframe = str(input("Choose timeframe: "))
    else:
        os.system('clear')
        quit()

    
    os.system('clear')
    output = subprocess.getoutput(f'curl -s rate.sx/{ticker}@{timeframe}')
    print(output)



main()
