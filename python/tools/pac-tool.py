import os
import subprocess
import time



def Welcome():
    os.system('clear')
    print(' ▄    ▄ ▄▄▄▄▄  ▄▄▄▄     ▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄')
    print(' █    █ █   ▀█ █   ▀▄   ██     █    █      █   ▀█')
    print(' █    █ █▄▄▄█▀ █    █  █  █    █    █▄▄▄▄▄ █▄▄▄▄▀')
    print(' █    █ █      █    █  █▄▄█    █    █      █   ▀▄')
    print(' ▀▄▄▄▄▀ █      █▄▄▄▀  █    █   █    █▄▄▄▄▄ █    ▀')
    print('\n')
    print('WHAT WOULD YOU LIKE TO DO?')
    print('\n')
    print('1 - UPDATE SYSTEM PACKAGES')
    print('2 - UPDATE AUR PACKAGES')
    print('3 - UPDATE PACMAN MIRROR LIST')
    print('4 - SEARCH SYSTEM FOR PACKAGE INFO')
    print('5 - PACKAGE LIST')
    print('6 - UN-USED PACKAGE LIST')
    print('7 - INSTALL A PACKAGE')
    print('8 - REMOVE A PACKAGE')
    print('9 - INSTALL AUR PACKAGE')
    print('10 - REMOVE AUR PACKAGE')
    print('\n')


    msg = input(': ')


    if msg == 'q':
        os.system('clear')
        quit()
    elif msg == '1':
        SysUpdate()
        Welcome()
    elif msg == '2':
        Yayup()
        Welcome()
    elif msg == '3':
        MirrorList()
        Welcome()
    elif msg == '4':
        PKG_Search()
        Welcome()
    elif msg == '5':
        PKG_List()
        Welcome()
    elif msg == '6':
        UN_USED_PKGS()
        Welcome()
    elif msg == '7':
        PKG_INSTALL()
        Welcome()
    elif msg == '8':
        PKG_REMOVE()
        Welcome()
    elif msg == '9':
        PKG_INSTALL()
        Welcome()
    elif msg == '10':
        PKG_REMOVE()
        Welcome()
    else:
        Welcome()




def SysUpdate():
    os.system('clear')
    print('LOOKING FOR UPDATES')
    time.sleep(1)
    os.system('sudo pacman -Syyu')
    os.system('clear')
    print('UPDATE COMPLETE')
    time.sleep(2)


def Yayup():
    os.system('clear')
    print('SEARCHING FOR AUR UPDATES')
    time.sleep(1)
    os.system('yay -Syyu')
    os.system('clear')
    print('AUR UPDATE COMPLETE')
    time.sleep(2)


def MirrorList():
    os.system('clear')
    print('SEARCHING FOR FASTEST MIRRORS...')
    time.sleep(1)
    os.system('sudo pacman-mirrors -ic United_States')
    print('UPDATING TO NEW MIRRORS...')
    time.sleep(2)
    os.system('sudo pacman-mirrors -f 5')
    print('NEW MIRROR LIST HAS BEEN APPLIED.')
    time.sleep(2)


def PKG_Search():
    os.system('clear')
    print('SEARCH BY PACKAGE NAME...', '\n')
    pkg_name = input(': ')
    if pkg_name == 'q':
        quit()
    else:
        os.system('clear')
        print('PACKAGE NAME')
        print('\n')
        print(pkg_name)
        pkg = subprocess.getoutput('pacman -Q | grep ' + pkg_name)
        print('-' + pkg)
        time.sleep(1)
        pkg_info = subprocess.getoutput('pacman -Si ' + pkg_name)
        print('\n')
        print(pkg_info)
        time.sleep(10)
        Welcome()


def PKG_List():
    os.system('clear')
    print('GENERATING PACKAGE LIST...')
    time.sleep(1)
    packages = subprocess.getoutput('pacman -Q | less')
    print(packages)
    leave = input(': ')
    if leave != 'q':
        time.sleep(600)
    else:
        Welcome()


def UN_USED_PKGS():
    os.system('clear')
    print('SEARCHING FOR UN-USED PACKAGES...', '\n')
    time.sleep(1)
    un_used = subprocess.getoutput('sudo pacman -Qdt')
    removable_pkg = un_used.split()
    removable_pkg = removable_pkg[::2]
    print(un_used)
    time.sleep(1)
    print('\n')
    remove_unused = input('WOULD YOU LIKE TO REMOVE UN-USED PACKAGES? (y/n) : ')
    if remove_unused != 'y':
        os.system('clear')
        print('RE-DIRECTING TO MAIN MENU')
        Welcome()
    else:
        print(removable_pkg)
        for x in removable_pkg:
            os.system('sudo pacman -Rns ' + x)
    os.system('clear')
    print('RE-DIRECTING TO MAIN MENU...')
    time.sleep(1)
    Welcome()


def PKG_INSTALL():
    os.system('clear')
    print('ENTER PACKAGE TO INSTALL', '\n')
    install_input = input(': ')
    if install_input != 'q':
        os.system('sudo pacman -S ' + install_input)
        time.sleep(1)
        os.system('clear')
        print('PACKAGE HAS BEEN INSTALLED')
        time.sleep(1)
        Welcome()
    else:
        os.system('clear')
        print('RE-DIRECTING TO MAIN MENU...')
        Welcome()


def PKG_REMOVE():
    os.system('clear')
    print('ENTER PACKAGE TO REMOVE', '\n')
    remove_input = input(': ')
    if remove_input != 'q':
        os.system('sudo pacman -Rns ' + remove_input)
        time.sleep(1)
        os.system('clear')
        print('PACKAGE HAS BEEN REMOVED')
        time.sleep(1)
        Welcome()
    else:
        os.system('clear')
        print('RE-DIRECTING TO MAIN MENU...')
        Welcome()



def AUR_INSTALL():
    os.system('clear')
    print('ENTER AUR PACKAGE TO INSTALL', '\n')
    aur_install_input = input(': ')
    if aur_install_input != 'q':
        os.system('yay -S ' + aur_install_input)
        time.sleep(1)
        os.system('clear')
        print('AUR PACKAGE HAS BEEN INSTALLED')
        time.sleep(1)
        Welcome()
    else:
        os.system('clear')
        print('RE-DIRECTING TO MAIN MENU...')
        Welcome()


def AUR_REMOVE():
    os.system('clear')
    print('ENTER AUR PACKAGE TO REMOVE', '\n')
    aur_remove_input = input(': ')
    if aur_remove_input != 'q':
        os.system('yay -Rns ' + aur_remove_input)
        time.sleep(1)
        os.system('clear')
        print('AUR PACKAGE HAS BEEN REMOVED')
        time.sleep(1)
        Welcome()
    else:
        os.system('clear')
        print('RE-DIRECTING TO MAIN MENU...')
        Welcome()




Welcome()


