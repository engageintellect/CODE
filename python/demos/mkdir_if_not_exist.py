import os
import subprocess
import time

# get username
usr = os.getcwd()
usr = usr.replace("/home/", "")

# make download folder is not there already.
path = os.listdir()

try:
    if 'tester' in path:
        os.chdir('videos')
        os.mkdir('youtube')
    else:
        os.chdir('/home/' + usr)
        os.mkdir('videos')
        os.chdir('videos')
        os.mkdir('youtube')

