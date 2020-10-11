# DICTIONARY


# MAKE NEW DICT
info = {'name':'josh', 'age':32}

# PRINT IT OUT
print(info)
print('\n')

# ADD SOMETHING USING UPDATE METHOD
info.update({'address':'irvine'})

# PRINT IT OUT
print('updated info is: ', info)
print('\n')

# ADD SOMETHING USING SUBSCRIPT NOTATION
info['book'] = 'fightclub'

# PRINT IT OUT
print(info)
print('\n')


# PRINT SOMETHING FROM DICT
print(info['age'])
print('\n')


# ITERATE (loop) THROUGH DICT AND PRINT KEYS AND VALUES
for x in info:
    print(x, '->', info[x])

print('\n')


#
