# 1. seperate str & int items from list
# 2. write sorted lists to file

import os

mylist = []

numbers = []
words = []

def main():
    os.system('clear')
    print('ADD SOMETHING TO LIST..' + '\n')
    for x in mylist:
        print(x)
    add_list()

def add_list():
    user_input = input(': ')
    while user_input != 'q':
        mylist.append(user_input)
        for x in mylist:
            print(x)
        main()
    else:
        sort_lists()
        quit()

def sort_lists():
    for x in mylist:
        try:
            x = int(x)
            numbers.append(x)
        except:
            x = str(x)
            words.append(x)
    print('\n')
    print('NUMBERS: ', numbers)
    print('WORDS: ', words)
    write_file()

    
def write_file():
    with open ('pull_int_from_list.txt', 'w') as myfile:
        myfile.write('NUMBERS: ' + str(numbers) + '\n')
        myfile.write('WORDS: ' + str(words))


main()
