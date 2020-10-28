import os
import subprocess

os.system('clear')

OUTPUT = subprocess.getoutput('acpi -V -f')
OUTPUT = OUTPUT.split('\n')
OUTPUT[1] = OUTPUT[1].replace('Unknown, ','')


ACPI_CONTENT = OUTPUT[1] + '\n' + OUTPUT[2] + '\n' + OUTPUT[4] + '\n' 


a = ACPI_CONTENT.split('\n')

for x in a:
    print(x)


THERMALS = a[2]


os.system('notify-send ' + "'" + THERMALS + "'")
