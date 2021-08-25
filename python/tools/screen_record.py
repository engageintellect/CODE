#!/usr/bin/env python3


import os
import subprocess
from time import sleep

screen_res = 0


# CLEAR THE SCREEN
def clear_screen():
    os.system('clear && figlet "SCREEN RECORD"')
    print('\n')

# GET DISPLAY RESOLUTION
def get_resolution():
    res = subprocess.getoutput("xrandr | grep connected | grep primary | awk '{print $4}' | sed 's/+0+0//g'")
    return res

# RECORD THE SCREEN
def record_screen():
    file_out = input("NAME VIDEO OUTPUT: ")
    if file_out != 'q':
        res = get_resolution()
        path = subprocess.getoutput('echo $HOME')
        os.chdir(path)
        cmd = f'ffmpeg -f x11grab -s {res} -r 25 -i :0.0 {file_out}.mp4'
        os.system(cmd)

        clear_screen(); print(f'SAVING FILE {file_out}'); sleep(1)
        os.system('clear')
    else:
        os.system('clear')
        quit()





# MAIN RUN
if __name__ == "__main__":
    clear_screen()
    record_screen()


