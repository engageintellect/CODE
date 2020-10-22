#!/usr/bin/env python3

import subprocess
import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
subprocess.call('clear', shell=True)
colorama.init()

print_lock = threading.Lock()

ip = input("Enter IP to scan: ")
port_range = input("Enter port range to scan (Default=1024): ")

if port_range == "":
    port_range = 1024
else:
    port_range = int(port_range)
    

print('\n')

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]======[" + Fore.GREEN + "Open" + Fore.RESET + "]")
    except:
        pass


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(port_range):
        executor.submit(scan, ip, port + 1)
    
