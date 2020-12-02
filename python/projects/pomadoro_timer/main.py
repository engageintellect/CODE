#!/usr/bin/env python3

import os
from playsound import playsound
from time import sleep


def main():
    os.system('clear')
    select_time = input("Enter time in minutes: ")

    if select_time == 'q':
        quit()
    elif select_time == '':
        os.system('clear')
        print("Default timer set for 15 minutes.")
        sleep(15*60)
        playsound('/home/r3dux/media/sounds/alarm.mp3')
        timer()
    else:
        sleep(int(select_time)*60)
        playsound('/home/r3dux/media/sounds/alarm.mp3')
        timer()




main()
