import os
os.system('clear')

# CLASSES
class People():
    def __init__(self, name, age, weight):
       self.name = name
       self.age = age
       self.weight = weight

    def display(self):
        print('\n')
        print('NAME:', self.name)
        print('AGE:', self.age)
        print('WEIGHT:', self.weight)

print('\n')
input_name = input('ENTER NAME: ')
input_age = input('ENTER AGE: ')
input_weight = input('ENTER WEIGHT: ')

os.system('clear')

Person1 = People(input_name, input_age, input_weight)
Person1.display()
