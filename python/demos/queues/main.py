import queue

# FIRST IN FIRST OUT

q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]

for number in numbers:
    q.put(number)

print('FIFO')
print(q.get())


# FIRST IN FIRST OUT
qLastInFirstOUut = queue.LifoQueue()

numbers = [10, 20, 30, 40, 50, 60, 70]

for number in numbers:
    qLastInFirstOUut.put(number)


print('FILO')
print(qLastInFirstOUut.get())



# PRIORITY QUEUE
qPriority = queue.PriorityQueue()

qPriority.put((2, 'hello world'))
qPriority.put((10, 99))
qPriority.put((1, 'hi'))
qPriority.put((3, True))



print('PRIORITY')
while not qPriority.empty():
    print(qPriority.get())

