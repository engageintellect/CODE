#!/usr/bin/env python


mylist = [
    {'name': 'josh', 'age':32},
    {'name': 'chris', 'age':20},
    {'name': 'jim', 'age':20},
    {'name': 'seteve', 'age':20},

]


class People():
    def __init__ (self, num, name, age):
        self.num = num
        self.name = name
        self.age = age

    def sayhi(self):
        print(f'hello {self.name}, you are {self.age} years old.')
        return "name:", self.name





x = People(1, 'josh', 33)
print(x.sayhi())


for x in mylist:
    if x['name'] == 'josh':
        print(f'found', x['name'])




