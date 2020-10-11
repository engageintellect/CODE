from itertools import cycle
import time

for c in cycle('/-\|'):
    print(c, end = '\r')
    time.sleep(0.1)
