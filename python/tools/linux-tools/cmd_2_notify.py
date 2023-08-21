import os
import subprocess


def dunster():
    usr_input = input(': ')
    
    notify_cmd = 'notify-send "$(' + usr_input + ')"'
    
    subprocess.call(notify_cmd, shell=True)

    dunster()

dunster()
