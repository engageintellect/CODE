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
    if tempf > 180:
        display()
        print('CPU TOO HOT!!! SHUTTING DOWN')
        sleep(3)
        quit()
    if tempf > 170:
        tempf = colored(f'TEMP: {tempf} F', 'red')
    elif tempf < 160:
        tempf = colored(f'TEMP: {tempf} F', 'blue')
    else:
        tempf = colored(f'TEMP: {tempf} F', 'green')
    return tempf
   

# CPU_HZ
def get_cpu_speed_hz():
    cpu_speed = subprocess.getoutput('vcgencmd measure_clock arm') \
            .replace('frequency', '').replace('(48)=', '')
    cpu_speed = f'FREQ: {cpu_speed} HZ'
    return colored(cpu_speed, 'green')


# CPU_GHZ
def get_cpu_speed_ghz():
    cpu_speed = subprocess.getoutput('vcgencmd measure_clock arm') \
            .replace('frequency', '').replace('(48)=', '')
    cpu_speed = f'FREQ: {float(cpu_speed)/1000000000} GHZ'
    return colored(cpu_speed, 'green')


# GET TIME DATA
def get_date_time():
    date_time = subprocess.getoutput("date | awk '{print $4}'")
    return colored(date_time, 'red')


# MAIN
def main():
    display()
    x = 0
    while True:
        x=x+1
        print(f'| {get_date_time()} | {get_temp()} | {get_cpu_speed_hz()} | {get_cpu_speed_ghz()} |')
        print('\n')
        sleep(5)
        if x != 20:
            continue
        else:
            main()


if __name__ == "__main__":
    main()

