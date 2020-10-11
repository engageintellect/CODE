# 1. seperate str & int items from list
# 2. write sorted lists to file

# original list
mylist = ['apple', 'banana', 3, 7, 'ice', 'cheetos', 'funyuns', 10, 22]

# sorted lists
numbers = []
words = []

# where the magic happens...
for x in mylist:
    print(x)
    try:
        x = int(x)
        numbers.append(x)
    except:
        x = str(x)
        words.append(x)

# print new/sorted lists
print('\n')
print('NUMBERS: ', numbers)
print('WORDS: ', words)


# write sorted lists to file(pull_int_from_list.txt)
with open ('pull_int_from_list.txt', 'w') as myfile:
    myfile.write('NUMBERS: ' + str(numbers) + '\n')
    myfile.write('WORDS: ' + str(words))





