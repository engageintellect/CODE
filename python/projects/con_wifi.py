#!/usr/bin/env python3

import os
import subprocess
from time import sleep

subprocess.call('clear')
disconnect = subprocess.call('iwctl station wlan0 disconnect kind-baer-5g', shell=True)


dev_list = subprocess.getoutput('iwctl device list')

for x in dev_list.split(" "):
    if "wlan" in x:
        dev_name = str(x)

# scan = subprocess.getoutput(f"iwctl station {dev_name} scan")
get_networks = subprocess.getoutput(f"iwctl station {dev_name} get-networks")


try:
    for x in get_networks.split():
        if "kind-baer-5g" in x:
            home_network = x
    connect_home = subprocess.getoutput(f"iwctl station {dev_name} connect {home_network}")
except:
    print(get_networks)
    choose_network = input("enter a network name to connect to: ")
    connect_manual = subprocess.getoutput("iwctl station {dev_name} connect {choose_network}")


print(f"Successfully connected to {home_network}"); sleep(2); subprocess.call('clear')




