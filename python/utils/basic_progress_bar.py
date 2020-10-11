from progress.bar import Bar
import time

with Bar('PROGRESS:', max=20) as bar:
    for i in range(20):
        time.sleep(0.2)
        # Do some work
        bar.next()
