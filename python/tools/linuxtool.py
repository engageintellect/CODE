
#  _     _                    _____           _
# | |   (_)_ __  _   ___  __ |_   _|__   ___ | |
# | |   | | '_ \| | | \ \/ /   | |/ _ \ / _ \| |
# | |___| | | | | |_| |>  <    | | (_) | (_) | |
# |_____|_|_| |_|\__,_/_/\_\   |_|\___/ \___/|_|
#  
# Verion:    1.0
# Build:     ThinkPad X220
# OS:        Manjaro-i3 Linux
#
#!/usr/bin/python3
import os
import time # time.sleep(sec)

# sh = bash 
sh = os.system

# ENTER SCREEN
def mainmenu():
    sh('clear')
    print("\n\n", "HACKING NETWORKS WITHOUT THE OWNERS PERMISSION IS ILLEGAL.", "\n\n")
    print("Have good judgement, do the right thing....", "\n\n")
    print("Type 'y' to enter or 'n' to quit.  ", "\n")
    enter = input(">  ")
    sh('clear')
    if enter == 'y':
        fallback()
    if enter == 'q':
        quit()
    if enter == 'n':
        quit()
    else:
        mainmenu()

# MAIN MENU
def fallback():
    sh('clear')
    print("  _     _                    _____           _")
    print(" | |   (_)_ __  _   ___  __ |_   _|__   ___ | |")
    print(" | |   | | '_ \| | | \ \/ /   | |/ _ \ / _ \| |")
    print(" | |___| | | | | |_| |>  <    | | (_) | (_) | |")
    print(" |_____|_|_| |_|\__,_/_/\_\   |_|\___/ \___/|_|")
    print("Welcome to Josh's Python3 powered Linux tool..", "\n")
    print("Version 1.0 2020.")
    print("https/github.com/jc9361", "\n\n")
    print("What would you like to do?", "\n")
    print("1  =  View System Specifications.")
    print("2  =  View System Proccesses.")
    print("3  =  View System Monitor.")
    print("4  =  Scan Local Network.")
    print("5  =  IP Scanner.")
    print("6  =  fsociety.")
    print("7  =  Social Engineering Toolkit.")
    print("8  =  Update System Packages.")
    print("9  =  Update AUR Packages.")
    print("0  =  SSH Portal")
    print("\n")
    print("99 = EXIT.")
    print("\n")
    fallback_menu = input(">  ")
    sh('clear')

    if fallback_menu == '1':
        neofetch()
    if fallback_menu == '2':
        htop()
    if fallback_menu == '3':
        ytop()
    if fallback_menu == '4':
        arpscan()
    if fallback_menu == '5':
        ipscan()
    if fallback_menu == '6':
        fsociety()
    if fallback_menu == '7':
        setoolkit()
    if fallback_menu == '8':
        syscheck()
    if fallback_menu == '9':
        aurupdate()
    if fallback_menu == '0':
        portal()
    if fallback_menu == '99':
        quit()
    if fallback_menu == 'q':
        quit()

# ESCAPE SEQUENCE
def exitscreen():
    print("\n", "99 = Back To Main Menu", "\n")
    goback = input(">  ")
    if goback == '99':
        fallback()

#PROGRAM FUNCTIONS
def portal():
    sh('clear')
    print("CHOOSE A MACHINE TO CONNECT TO.", "\n\n")
    print("1  =  Surface Book 2")
    print("2  =  Macbook Pro")
    print("3  =  ThinkPac X220", "\n\n")
    print("99 = Back To Main Menu", "\n")
    whichssh = input(">  ")
        
    sh('clear')

    if whichssh == '99':
        fallback()
    if whichssh == '1':
        sh('ssh 192.168.1.29')
        portal()
    if whichssh == '2':
        sh('ssh 192.168.1.25')
        portal()
    if whichssh == '3':
        sh('ssh 192.168.1.11')
        portal()

def setoolkit():
    sh('clear')
    print("TAKING YOU TO THE SOCIAL ENGINEERING TOOLKIT...", "\n\n")
    time.sleep(2)
    sh('sudo setoolkit')
    fallback()

def fsociety():
    sh('clear')
    print("TAKING YOU TO FSOCIETY...", "\n\n")
    time.sleep(2)
    sh('python2 ~/Code/hacking/fsociety/fsociety.py')
    fallback()
    
def neofetch():
    sh('neofetch')
    exitscreen()

def htop():
    sh('htop')
    fallback()

def arpscan():
    time.sleep(1)
    print("SCANNING LOCAL WIFI NETWORK", "\n")
    time.sleep(1)
    sh('sudo arp-scan --localnet')
    time.sleep(1)
    print("\n\n", "Copy the ip address of your target for IP scan...", "\n\n")
    exitscreen()

def ytop():
    sh('ytop')
    fallback()
        
def ipscan():
    print("Enter ip to scan", "\n")
    ip = input(">  ")
    if ip == 'q':
        fallback()
    cmd = "sudo nmap -sn" + " " + ip
    print("\n", "SCANNING MACHINE @", ip, "\n")
    time.sleep(1)
    os.system(str(cmd)) 
    exitscreen()

# SYSTEM CHECK
def syscheck():
    print("Are you running an arch based distro or debian?", "\n\n")
    print("1  =  Arch")
    print("2  =  Debian", "\n\n")
    print("99 = Back To Main Menu", "\n")
    distro = input(">  ")

    sh ('clear')

    if distro == '99':
        fallback()
    if distro == 'q':
        fallback()
    if distro == '1':
        pacupdate()
    if distro == '2':
        aptupdate()

# APT UPDATE
def aptupdate():
    time.sleep(1)
    print("SCANNING FOR AVAILABLE UPDATES.", "\n\n")
    time.sleep(1)
    sh('sudo apt update')
    time.sleep(1)
    print("\n\n")
    print("SCAN COMPLETE", "\n\n")
    time.sleep(1)
    print("SCANNING FOR UPGRADES.", "\n\n")
    time.sleep(1)
    sh('sudo apt upgrade -y')
    time.sleep(1)
    print("\n\n")
    print("UPGRADE COMPLETE", "\n\n")
    time.sleep(3)
    fallback()

# PACMAN UPDATE
def pacupdate():
    time.sleep(1)
    print("SCANNING FOR AVAILABLE UPDATES.", "\n\n")
    time.sleep(1)
    sh('sudo pacman -Syy')
    time.sleep(1)
    print("\n\n")
    print("SCAN COMPLETE", "\n\n")
    time.sleep(1)
    print("SCANNING FOR UPGRADES.", "\n\n")
    time.sleep(1)
    sh('sudo pacman -Syu')
    time.sleep(1)
    print("\n\n", "UPGRADE COMPLETE", "\n\n")
    time.sleep(3)
    fallback()

# AUR UPDATE
def aurupdate():
    time.sleep(1)
    print("UPDATING THE ARCH USER REPOSITORY.", "\n\n")
    time.sleep(1)
    sh('yay -Syy')
    time.sleep(1)
    print("\n\n")
    print("UPDATE COMPLETE", "\n\n")
    time.sleep(1)
    print("SCANNING ARCH USER REPOSITORY FOR UPGRADES", "\n\n")
    sh('yay -Syu')
    time.sleep(1)
    print("ARCH USER REPOSITORY IS UP TO DATE.", "\n\n")
    time.sleep(3)
    fallback()

mainmenu()
