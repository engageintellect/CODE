import os
import subprocess
import time


# MAIN PROGRAM
def MainLoop():

    # GET ACPI BATTERY STATUS
    COMMAND = subprocess.getoutput('acpi -b')

    # CLEAN UP OUTPUT
    CMD_OUT = COMMAND.replace("Battery 0: ",'')

    # CHOP UP OUTPUT AND ADD TO LIST
    OUTPUT_LIST = CMD_OUT.split(",")

    # NOTIFY COMMAND
    DUNST_CMD = f'notify-send "{CMD_OUT}"'
   
    # SEND NOTIFICATION
    NOTIFY = os.system(DUNST_CMD)

    # SLEEP TIME (in seconds)
    time.sleep(1500)

    MainLoop()


MainLoop()



