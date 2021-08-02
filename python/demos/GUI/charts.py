#!/usr/bin/env python3

### IMPORTS ###
import PySimpleGUI as sg
import os
import requests


### CLEAR DISPLAY ###
def display():
    os.system('clear')


### LAYOUT ###
layout = [[sg.Text("PICK AN OPTION")], 
        [sg.Button("BTC")], 
        [sg.Button("ETH")], 
        [sg.Button("DOGE")], 
        [sg.Button("ADA")], 
        [sg.Button("QUIT")]]


### WINDOW ###
window = sg.Window("helloworld", layout, margins=(25, 25))


### EVENT LOOP ###
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "QUIT" or event == sg.WIN_CLOSED:
        display()
        break
    elif event == "BTC":
        display()
        print(requests.get('https://rate.sx/btc').text)
    elif event == "ETH":
        display()
        print(requests.get('https://rate.sx/eth').text)
    elif event == "DOGE":
        display()
        print(requests.get('https://rate.sx/doge').text)
    elif event == "ADA":
        display()
        print(requests.get('https://rate.sx/ada').text)

window.close()
