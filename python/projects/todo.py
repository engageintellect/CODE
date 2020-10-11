import os
import time

mylist = []

def draw_banner():
    os.system('clear')
    print(" _____     ____")
    print("|_   _|__ |  _ \  ___    _")
    print("  | |/ _ \| | | |/ _ \  (_)")
    print("  | | (_) | |_| | (_) |  _")
    print("  |_|\___/|____/ \___/  (_)")
    print(" _____ _____ _____ _____ _____")
    print("|_____|_____|_____|_____|_____|")
    print("\n")

    read_and_convert()

def read_and_convert():
    try:
        with open ('todo.json', 'r') as myfile:
            a = myfile.read()
            a = a.replace(",", "")
            a = a.replace("'", "")
            a = a.replace("[", "")
            a = a.replace("]", "")
            a = a.split()
            for x in a:
                mylist.append(x)

            for x in mylist:
                print(x)
            print("\n")

            list_input()
    except:
        list_input()



def save_list():
    with open ('todo.json', 'w') as myfile:
        myfile.write(str(mylist))
        os.system('clear')
        print('Saving file as "todo.json"...')
        time.sleep(1)
        quit()

def list_input():
    usr_input = input('> ')

    while usr_input != 'q':
        mylist.append(usr_input)
        list_input()
    else:
        save_list()


def display():
    draw_banner()
    for x in mylist:
        print(x)
    


draw_banner()
