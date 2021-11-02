#!/usr/bin/env python3

#####################################
### A script to monitor CPU temp. ###
#####################################



import os
import subprocess
from termcolor import colored
from time import sleep




def display():
    os.system('clear')
    os.system('figlet "Pi - TEMP"')
    print('******************************************')
    print('\n')
    sleep(1)


# CPU_TEMP
def get_temp():
    temp = subprocess.getoutput('/opt/vc/bin/vcgencmd measure_temp')
    temp = float(temp.replace('temp=', '').replace("'C", ''))
    tempf = int(temp*1.8+32)
    if tempf > 170:
        tempf = colored(f'TEMP: {tempf} F', 'red')
    else:
        tempf = colored(f'TEMP: {tempf} F', 'green')
    return tempf
   

# CPU_HZ
def get_cpu_speed_hz():
    cpu_speed = subprocess.getoutput('vcgencmd measure_clock arm') \
            .replace('frequency', '').replace('(48)=', '')
    cpu_speed = f'FREQ: {cpu_speed} HZ'
    return cpu_speed


# CPU_GHZ
def get_cpu_speed_ghz():
    cpu_speed = subprocess.getoutput('vcgencmd measure_clock arm') \
            .replace('frequency', '').replace('(48)=', '')
    cpu_speed = f'FREQ: {float(cpu_speed)/1000000000} GHZ'
    return cpu_speed


# MAIN
def main():
    display()
    x = 0
    while True:
        x=x+1
        print(get_temp())
        print(get_cpu_speed_hz())
        print(get_cpu_speed_ghz())
        print('\n')
        sleep(5)
        if x != 20:
            continue
        else:
            main()


if __name__ == "__main__":
    main()

