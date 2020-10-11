import time
from progress.bar import PixelBar

mylist = [1,2,3,4,5,6,7,8,9,10]

bar = PixelBar('PROGRESS', max = len(mylist))

for item in mylist:
    bar.next()
    time.sleep(1)

bar.finish()
