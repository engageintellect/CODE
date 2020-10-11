import sys
import time
import threading
import subprocess
import os

class progress_bar_loading(threading.Thread):

    def run(self):
            global stop
            global kill
            os.system('clear')
            print('PROCESSING...')
            sys.stdout.flush()
            i = 0

            while stop != True:
                if (i%4) == 0:
                    sys.stdout.write('\b/')
                elif (i%4) == 1:
                    sys.stdout.write('\b-')
                elif (i%4) == 2:
                    sys.stdout.write('\b\\')
                elif (i%4) == 3:
                    sys.stdout.write('\b|')

                sys.stdout.flush()
                time.sleep(0.1)
                i+=1

            if kill == True:
                os.system('clear')
                print('ABORT')
            else:
                os.system('clear')
                print('COMPLETE')

kill = False
stop = False
p = progress_bar_loading()
p.start()
                

try:
    # ANYTHING YOU WANNA RUN
    time.sleep(4)
    stop = True
except KeyboardInterrupt or EOFError:
        kill = True
        stop = True
