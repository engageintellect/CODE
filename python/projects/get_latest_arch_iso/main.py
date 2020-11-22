#!/usr/bin/env python3

import subprocess, os, sys
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://archlinux.org/download")

link = driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul[2]/li[2]/a')
link.click()

sleep(3)

driver.close()
path = os.getcwd()
os.chdir('/home/r3dux/downloads')
dir_contents = os.listdir()

for x in dir_contents:
    if "archlinux" in x:
        arch_torrent = str(dir_contents[x.index("archlinux")])

subprocess.call(f'transmission-cli -f "{path}/kill_transmission.sh" {arch_torrent}', shell=True)


os.system('clear')
print('LATEST ARCH ISO HAS BEEN DOWNLOADED')


# CLEAN UP
try:
    dir_contents = os.listdir()
    for x in dir_contents:
        if ".torrent" in x:
            subprocess.call(f'rm {x}', shell=True)
    
    os.system('cd /home/r3dux/.config/transmission/torrents && rm *')
    os.system('cd /home/r3dux/.config/transmission/resume && rm *')
except:
    print("no files to clean up... moving on...")

for x in os.listdir():
    if "arch" in x:
        iso_file = x
os.system(f'mv {iso_file} archlinux.iso')


print(f"Ready to burn ISO image [{iso_file}] to disk")
















 
