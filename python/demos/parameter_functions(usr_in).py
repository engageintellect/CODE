# FUNCTIONS WITH PARAMETER EXAMPLE

#!/usr/bin/env python

name = None
num = 0

def say_hello(name):
    name = input("what is your name? ")
    if name == '':
        print('Hi!')
    else:
        print(f'hello {name}')

def change_sign(num):
    num = int(input("enter a number: "))
    return num * -1

 
def square_num(num):
    num = int(input('num: '))
    return num*num*num



say_hello(name)
print("your number inverted is:", change_sign(num))
print("your number squared is", square_num(num))

