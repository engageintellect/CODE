#!/usr/bin/env python3

import subprocess
import socket
import colorama
from colorama import Fore
subprocess.call("clear", shell=True)

colorama.init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set timeout (optional)
s.settimeout(5)

host = input( "Enter an IP to scan: ")
port = int(input("Enter a port number: "))


def portScanner(port):
    print("\n")

    if s.connect_ex((host, port)):
        print(f"PORT [{port}] IS " + Fore.RED + "CLOSED\n")
    else:
        print(f"PORT [{port}] IS " + Fore.GREEN + "OPEN\n")



portScanner(port)
