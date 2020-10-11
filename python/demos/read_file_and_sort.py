newlist = []

numbers = []
words = []

try:
    with open('pull_int_from_list.txt', 'r') as myfile:
        readfile = myfile.read()
    a = readfile.split()
    del(a[0])
    del(a[3])
    for x in a:
        x = x.strip(',')
        x = x.strip('[')
        x = x.strip(']')
        x = x.strip("'")
        newlist.append(x)
    for x in newlist:
        try:
            x = int(x)
            numbers.append(x)
        except:
            x = str(x)
            words.append(x)
    print('NUMBERS:', numbers)
    print('WORDS:', words)
except:
    print('hello world')
