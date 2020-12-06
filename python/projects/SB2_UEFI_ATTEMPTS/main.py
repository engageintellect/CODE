#!/usr/bin/env python3

import os
import subprocess
from time import sleep


os.system('clear')
pw_list = []



def main():
    x = 0
    while x<100:
        x+=1
        print(f"Attempt # {x}")
        user_input()


def user_input():
    attempt = input(">  ")
    if attempt == 'q':
        os.system('clear')
        write_file()
        print("Terminating Program..")
        sleep(1)
        os.system('clear')
        quit()
    else:
        pw_list.append(attempt)
        pass


def write_file():
    print("Writing File...")
    with open('attempts.txt', 'a') as pw_file:
        for x in pw_list:
            pw_file.write(x + "\n")
    sleep(1)
    print("File saved as 'attempts.txt'")
    sleep(1)


main()
