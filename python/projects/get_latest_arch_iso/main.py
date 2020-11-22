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
dir_contents = os.listdir()
for x in dir_contents:
    if ".torrent" in x:
        print(x)
        subprocess.call(f'rm {x}', shell=True)
    else:
        print("ready to burn iso")

subprocess.call('rm * "/home/r3dux/.config/transmission/torrents"', shell=True)
subprocess.call('rm * "/home/r3dux/.config/transmission/resume"', shell=True)
















 
