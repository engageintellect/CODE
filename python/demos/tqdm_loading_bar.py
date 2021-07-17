import os
from tqdm import *


def clear_screen():
    os.system('clear')



def loading():
    for i in tqdm(range(20,2000000)):
        a = []
        a.append(i)



def main():
    clear_screen()
    print('hello')
    loading()
    print('byebye')
    loading()
    clear_screen()


main()







