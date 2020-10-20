#!/usr/bin/env python3

import subprocess
import socket
import colorama
from colorama import Fore
subprocess.call("clear", shell=True)


colorama.init()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)


host = input( "Enter an IP to scan: ")
port_range = input( "Enter port range (default: 1024): ")
open_ports = []


if port_range == "":
    port_range = 1024
else:
    port_range = int(port_range)


def portScanner(port):
    if s.connect_ex((host, port)):
        pass
    else:
        open_ports.append(port)
        print(port)


def main():
    print("\n")
    for x in range (port_range):
        port = x
        portScanner(port)
    for x in open_ports:
        print(f"PORT [{x}] IS " + Fore.GREEN + "OPEN" + Fore.RESET)
    print("\n")

    
main()    
