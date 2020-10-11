# CLEANER EVEN OR ODD LAMBDA FUNCTION

x = int(input('Enter a number: '))

eeo = lambda x: print(' is even.') if x % 2 == 0 else print(x, ' is odd')

eeo(x)
