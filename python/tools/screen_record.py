#!/usr/bin/env python3


import os
import subprocess

screen_res = 0


def clear_screen():
    os.system('clear && figlet "SCREEN RECORD"')
    print('\n')


def get_resolution():
    res = subprocess.getoutput("xrandr | grep connected | grep primary | awk '{print $4}'")
    res = res.replace('+0+0', '')
    return res


def record_screen():
    file_out = input("NAME VIDEO OUTPUT: ")
    if file_out != 'q':
        pass
    else:
        os.system('clear')
        quit()

    res = get_resolution()
    cmd = f'ffmpeg -f x11grab -s {res} -r 25 -i :0.0 {file_out}.mp4'
    os.system(cmd)


def main():
    clear_screen()
    record_screen()
main()
