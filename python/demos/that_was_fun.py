import subprocess
import time

# THAT WAS FUN

usr_in = input(": "); usr_cmd = f"surf {usr_in}"; subprocess.call(usr_cmd, shell=True); \
        subprocess.call('clear', shell=True); time.sleep(1); subprocess.call('echo "that was fun"', shell=True); \
        time.sleep(1); subprocess.call('clear', shell=True)



