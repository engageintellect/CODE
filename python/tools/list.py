#              _   _                   _ _     _   
#  _ __  _   _| |_| |__   ___  _ __   | (_)___| |_ 
# | '_ \| | | | __| '_ \ / _ \| '_ \  | | / __| __|
# | |_) | |_| | |_| | | | (_) | | | | | | \__ \ |_ 
# | .__/ \__, |\__|_| |_|\___/|_| |_| |_|_|___/\__|
##|_|###|___/######################################                                     


# blank list
list = []


# Greeter

print('\n')
print('Welcome to PyList')
print('\n')
print('Start typing items to add them to your list.')
print('\n')
print("To save your list enter 's' and hit return. Enter 'q' and hit return to quit.")
print('\n')
print("You're list will be saved in your current directory as 'list.txt'. It will automatically update each time you make a new list.")
print('\n')


# function to write list to text file.
def write_list():
    with open('list.txt', 'w')as w:
        w.write(str(list))

    print(list)
    print('\n')
    print('DONE')

# function to add items to the list.
def add():

    addtolist = input('add items to list: ')

    if addtolist == 'q':
        quit()

    if addtolist == 's':
        write_list()
        print('List has been saved to current foler as "list.txt".')
        print('Exiting.')
        quit()

    else:
        list.append(addtolist)

        for x in list:
            print(x)

        add()


# start funtions
add()
