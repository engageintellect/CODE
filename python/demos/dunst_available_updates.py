import os
import subprocess

mylist = []

a = str(subprocess.getoutput('sudo pacman -Syyu'))

a = a.replace("'", "")
a = a.replace(",", "")
a = a.replace("[", "")
a = a.replace("]", "")

l = a.split()

for x in l:
    mylist.append(x)

a = str((l[-5:]))

a = a.replace("'", "")
a = a.replace(",", "")
a = a.replace("[", "")
a = a.replace("]", "")

if a == 'there is nothing to do':
    os.system('notify-send "NO UPDATES AVAILABLE"')
else:
    os.system('notify-send "UPDATES AVAILABLE"')


