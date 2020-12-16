#!/usr/bin/env python3

# PROGRAM DESCRIPTION: A PERSONAL ALEXA-LIKE ASSISTANT, CODED IN PYTHON.
# AUTHOR: r3dux

import os
import subprocess
from time import sleep
import speech_recognition as sr
import pyttsx3


assistant_name = 'Alex'
listener = sr.Recognizer()


def display():
    os.system('clear'); os.system(f'figlet [ {assistant_name} ]'); print('\n')

def clear_screen():
    os.system('clear')

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        display()
        print('Listening...\n')
        os.system('arecord -q -d 3 --device hw:0,0 --format s16_le --channels 2 --rate 48000 voice.wav')
        with sr.AudioFile("voice.wav") as source:
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()

            return command
    except:
        print("Sorry, I didn't catch that... Please repeat that for me.")
        talk("Sorry, I didn't catch that... Please repeat that for me.")
        sleep(1)
        listen()



def run_command():
    command = listen()
    if assistant_name.lower() not in command:
        command = command.replace(f'{assistant_name.lower()} ', '')
        display()
        print(f'COMMNAD: "{command}"\n')
                
        if 'search' in command:
            command = command.replace('search ', '')
            print(f'Searching for {command}.')
            talk(f'Searching for {command}.')
            search = f'$BROWSER "google.com/search?&q={command}"'
            os.system(search)
        elif 'go to' in command:
            command = command.replace("go to ", "")
            print(f'Opening {command}')
            talk(f'Opening {command}.')
            surf = f'$BROWSER {command}.com'
            os.system(surf)
        elif 'say' in command:
            command = command.replace('say ', '')
            talk(command)
        elif 'email' in command:
            os.system('st -n email -e mutt')
        elif 'code repo' in command:
            git_code = subprocess.getoutput("cd ~/code && git add . && git commit -m 'updating' && git push origin master")
            print(git_code)
            sleep(2)
        elif 'lower brightness' in command:
            os.system('brightnessctl set 20%-')
        elif 'increase brightness' in command:
            os.system('brightnessctl set 20%+')
        elif 'run system update' in command:
            os.system('st -e sudo pacman -Syu')
        elif 'system monitor' in command:
            os.system('st -n ytop -e ytop')
        elif 'restart' in command:
            os.system('sudo reboot')
        elif 'lockscreen' in command:
            os.system('slock')
        else:
            display()
            print(f"You need to say my name, '{assistant_name}' to issue your commnad.")
            talk(f"You need to say my name, '{assistant_name}' to issue your commnad.")

run_command()

