import os
import subprocess

os.system('clear')
cmd = subprocess.getoutput('sudo arp-scan --localnet')
cmd = cmd.split("\n")
cmd = cmd[2:]
cmd = cmd[:-3]

def INTERFACE_NAME():
    interface = subprocess.getoutput('sudo arp-scan --localnet')
    interface_chop = str(interface.split())
    interface_chop = interface_chop.replace(',','')
    interface_chop = interface_chop.replace('[','')
    interface_chop = interface_chop.replace(']','')
    interface_chop = interface_chop.replace("'",'')
    interface_chop = interface_chop.replace("Interface: ",'')
    interface_end = interface_chop.index('type:')
    print('NETWORK INTERFACE =', interface_chop[:int(interface_end)])

print(" _")
print("(_)_ __        ___  ___ __ _ _ __  _ __   ___ _ __")
print("| | '_ \ _____/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|")
print("| | |_) |_____\__ \ (_| (_| | | | | | | |  __/ |")
print("|_| .__/      |___/\___\__,_|_| |_|_| |_|\___|_|")
print("  |_|")
print("\n")
INTERFACE_NAME()
print('DEVICES ON NETWORK:')

n = 0
for x in cmd:
    n = n + 1
    print(str(n), "  ", str(x))

print('\n')

#for x in cmd:
#    print(x)


CMD_LENGTH = len(cmd)
if CMD_LENGTH > 0:
    s1 = str(cmd[0])
    s1 = s1.split()
    s1 = s1[0]

if CMD_LENGTH > 1:
    s2 = str(cmd[1])
    s2 = s2.split()
    s2 = s2[0]

if CMD_LENGTH > 2:
    s3 = str(cmd[2])
    s3 = s3.split()
    s3 = s3[0]

if CMD_LENGTH > 3:
    s4 = str(cmd[3])
    s4 = s4.split()
    s4 = s4[0]

if CMD_LENGTH > 4:
    s5 = str(cmd[4])
    s5 = s5.split()
    s5 = s5[0]

if CMD_LENGTH > 5:
    s6 = str(cmd[5])
    s6 = s6.split()
    s6 = s6[0]

if CMD_LENGTH > 6:
    s7 = str(cmd[6])
    s7 = s7.split()
    s7 = s7[0]

if CMD_LENGTH > 7:
    s8 = str(cmd[7])
    s8 = s8.split()
    s8 = s8[0]

if CMD_LENGTH > 8:
    s9 = str(cmd[8])
    s9 = s9.split()
    s9 = s9[0]

print("\n")
usr_input = input('ENTER IP TO SEARCH: ')

if usr_input == 'q':
    os.system('clear')
    quit()

if usr_input == 1:
    os.system('nmap -Pn ' + s1)
if usr_input == 2:
    os.system('nmap -Pn ' + s2)
if usr_input == 3:
    os.system('nmap -Pn ' + s3)
if usr_input == 4:
    os.system('nmap -Pn ' + s4)
if usr_input == 5:
    os.system('nmap -Pn ' + s5)
if usr_input == 6:
    os.system('nmap -Pn ' + s6)
if usr_input == 7:
    os.system('nmap -Pn ' + s7)
if usr_input == 8:
    os.system('nmap -Pn ' + s8)
if usr_input == 9:
    os.system('nmap -Pn ' + s9)


else:
    a = str(subprocess.getoutput('nmap -Pn ' + usr_input))
    os.system('clear')
    print(a + "\n")
    i = input('ENTER Q to GO BACK TO LIST: ')
    if i == 'q':
        os.system('clear')
        os.system('python3 ~/code/python/tools/arp_scanner.py')






