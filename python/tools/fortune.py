import os
import subprocess

# DISPLAY FORTUNE THROUGH COWSAY (TUX)
#f = subprocess.getoutput('fortune | cowsay -f tux')
f = subprocess.getoutput('fortune')

# DISPLAY FORTUNE BY ITSELF
#f = subprocess.getoutput('fortune')

print(f + '\n')


