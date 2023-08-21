import os
import subprocess
import time

os.system('clear')

print('REFRESHING MIRROR LIST')
time.sleep(2)

os.system('sudo pacman-mirrors -f 5')

os.system('clear')
print('FETCHING NEW MIRRORS')
time.sleep(2)

print('RUNNING PACMAN SYNC AND UPDATE')
os.system('sudo pacman -Syyu')

os.system('clear')

print('MIRROR UPDATE COMPLETE')
time.sleep(2)
quit()

