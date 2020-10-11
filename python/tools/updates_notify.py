#!/usr/bin/env python3


import os
import subprocess
from time import sleep



def update_checker():
    sleep(5)
    
    cmd = subprocess.getoutput('yay -Syu').split()
    
    
    if 'nothing' in cmd:
        subprocess.call('notify-send "NO UPDATES ARE AVAILABLE"', shell=True)
    else:
        notify = subprocess.call('notify-send "$(sudo pacman -Syu)"', shell=True)


    sleep(5)

    update_checker()



update_checker()
