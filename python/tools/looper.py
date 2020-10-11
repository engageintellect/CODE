import os
import subprocess
import time


# LOOPER THAT NOTIFIES TRUE AND FALSE CONDITIONS...

def looper():
    if subprocess.getoutput('pgrep -x chromium') == '':
        os.system('notify-send "CHROMIUM IS NOT OPEN"')
    else:
        while subprocess.getoutput('pgrep -x chromium') != '':
            os.system('notify-send "CHROME HAS BEEN OPENED"')
            time.sleep(3)
    
    time.sleep(3)
    looper()

looper()
