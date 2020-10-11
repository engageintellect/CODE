import os
import subprocess
import time

main_list = []

def Welcome():
    os.system('clear')
    print(' _____ ___  ____   ___')
    print('|_   _/ _ \|  _ \ / _ \ _')
    print('  | || | | | | | | | | (_)')
    print('  | || |_| | |_| | |_| |_')
    print('  |_| \___/|____/ \___/(_)')
    print('\n')

    for x in main_list:
        print(x)
    add_list()



def add_list():
    print('ADD ITEM TO LIST')

    add_input = input(': ')

    while add_input != 'q':
        main_list.append(add_input)
        with open('todo.txt', 'w')as w:
            w.write(str(main_list))
        Welcome()
    else:
        os.system('clear')
        print('TODO LIST HAS BEEN UPDATED')
        time.sleep(1)
        os.system('clear')
        quit()


Welcome()

