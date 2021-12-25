#!/usr/bin/env python3

import PySimpleGUI as sg
import requests
import os


layout = [[sg.Text("Hello World")], 
        [sg.Button("WEATHER")],
        [sg.Button("CLOSE")]
        ]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

    elif event == "WEATHER":
        os.system('python ~/code/python/projects/weather/local_weather.py')

window.close()
