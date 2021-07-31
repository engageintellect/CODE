#!/usr/bin/env python3


import os

def display():
    os.system('clear && figlet "SQUARE MAKER"')
    print('\n')


class Square():
    def __init__ (self, name,  width, height):
        self.name = name
        self.width = width
        self.height = height

    def describe_self(self):
        info = f'SQUARE: {self.name}\nHEIGHT: {self.height}\nWIDTH: {self.width}\n'
        print(info)

    def area(self):
        result = self.width*self.height
        print(f'AREA: {result}')

    def diameter(self):
        result = self.width*2+self.height*2
        print(f'DIAMETER: {result}')




def Square_Builder():
    display()
    name = str(input("ENTER NAME: "))
    height = int(input("ENTER HEIGHT: "))
    width = int(input("ENTER WIDTH: "))
    display()
    x = Square(name, height, width)
    Square.describe_self(x)
    Square.area(x)
    Square.diameter(x)




def main():
    Square_Builder()
main()

