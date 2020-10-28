import os
import subprocess

usr = input(": ")
cmd = f'notify-send "$({usr})"'

print(cmd)
notify = subprocess.call(cmd, shell=True)
