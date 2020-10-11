import os
import subprocess

# CLEAR SCREEN
subprocess.call('clear')

# USER INPUT
search_input = input("SEARCH FOR PKG: ")

# DUNST COMMAND
notify_cmd = 'notify-send -h string:bgcolor:$color0 -h string:fgcolor:$color2 \
             --urgency critical "$(pacman -Ss ' + search_input + ')"'

# RUN IT
subprocess.call(notify_cmd, shell=True)
