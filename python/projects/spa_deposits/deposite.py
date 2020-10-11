import os
import subprocess

os.system('clear')
os.system('touch test.txt')


print(' ____  _____ ____   ___  ____ ___ _____ ____')
print('|  _ \| ____|  _ \ / _ \/ ___|_ _|_   _/ ___|')
print('| | | |  _| | |_) | | | \___ \| |  | | \___ \ ')
print('| |_| | |___|  __/| |_| |___) | |  | |  ___) | ')
print('|____/|_____|_|    \___/|____/___| |_| |____/ ')
print('\n')

with open('deposit.txt', 'r')as r:
    r.read()

# GATHER USER INPUT 
name = input("ENTER CLIENT NAME: ")
email = input("ENTER CLIENT EMAIL: ")
print('\n')
deposit = input("HAS CLIENT PAID DEPOSIT?: ")
print('\n')

# LIST
list1 = []
list1.append("NAME: " + name + " " + "DEPOSIT PAID: " + deposit)

list_copy = str(list1)

with open('deposit.txt', 'a')as myfile:
    myfile.write(list_copy + '\n')

if deposit == 'yes':
    print('READY TO BOOK APPOINTMENT')
if deposit == 'Yes':
    print('READY TO BOOK APPOINTMENT')
if deposit == 'YES':
    print('READY TO BOOK APPOINTMENT')
if deposit == 'y':
    print('READY TO BOOK APPOINTMENT')
if deposit == 'Y':
    print('READY TO BOOK APPOINTMENT')

if deposit == 'no':
    print('CLIENT HAS NOT PAID DEPOSIT!' + '\n')
    print('SENDING LINK TO:' + email)
    
    




