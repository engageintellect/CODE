import os
import subprocess
import time

def main():

    os.system('clear')

    print("__     ______  _   _")
    print("\ \   / /  _ \| \ | |")
    print(" \ \ / /| |_) |  \| |")
    print("  \ V / |  __/| |\  |")
    print("   \_/  |_|   |_| \_|")
    print("\n")
    
    usr_input = input('> ')

    if usr_input == 'q':
        os.system('clear')
        quit()
    
    if usr_input == 'h':
        a = subprocess.getoutput('windscribe')
        print(a)
        time.sleep(3)
        main()

    if usr_input == 'stat':
        a = subprocess.getoutput('windscribe status')
        print(a)
        time.sleep(3)
        main()

    if usr_input == 'account':
        a = subprocess.getoutput('windscribe account')
        print(a)
        time.sleep(3)
        main()
    
    if usr_input == 'locations':
        a = subprocess.getoutput('windscribe locations')
        print(a)
        time.sleep(3)
        main()

    else:
        print('\n')
        os.system('windscribe ' + str(usr_input))




main()
