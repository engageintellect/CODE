n = int(input('enter a number: '))

eoo = lambda n: True if n % 2 == 0 else False

if eoo(n) == True:
    print(str(n) + ' is even')
else:
    print(str(n) + ' is odd')



