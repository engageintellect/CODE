#!/usr/bin/env python3

import os
from playsound import playsound
from time import sleep


def main():
    os.system('clear')
    display()
    select_time = input("Enter time in minutes: ")

    if select_time == 'q':
        print("Program Terminated"); sleep(1)
        os.system('clear')
        quit()
    elif select_time == '':
        os.system('clear')
        display()
        print("Default timer set for 15 minutes.")
        sleep(3)
        playsound('iphone_alarm_morning(short).mp3')
        timer()
    else:
        os.system('clear')
        display()
        print(f"Timer Started for {select_time} miutes")
        sleep(int(select_time)*60)
        playsound('iphone_alarm_alarm.mp3')
        timer()


def display():
    print(" _   _ ")
    print("| |_(_)_ __ ___   ___ _ __ ")
    print("| __| | '_ ` _ \\ / _ \\ '__| ")
    print("| |_| | | | | | |  __/ | ")
    print(" \\__|_|_| |_| |_|\\___|_| ")
    print("\n")


main()
