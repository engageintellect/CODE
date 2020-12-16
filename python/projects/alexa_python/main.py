#!/usr/bin/env python3

# PROGRAM DESCRIPTION: A PERSONAL ALEXA-LIKE ASSISTANT, CODED IN PYTHON.
# AUTHOR: r3dux

import os
import subprocess
from time import sleep
import speech_recognition as sr
import pyttsx3



#===[ NAME OF ASSISTANT ]===#
assistant_name = 'Alexa'

#===[ INITIALIZE LISTENER ]===#
listener = sr.Recognizer()

#===[ INITIALIZE VOICE ENGINE ]===#
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
rate = engine.setProperty('rate', 175)


#===[ DISPLAY FUNCTIONS ]===#
def display():
    os.system('clear'); os.system('figlet [ Alexa ]'); print('\n')
def clear_screen():
    os.system('clear')



#===[ RECORD VOICE TO FILE (MICROPHONE WORKAROUND) ]===#

def main():
    try:
        display()
        print('Listening...\n')
        os.system('arecord -d 3 --device hw:0,0 --format s16_le --channels 2 --rate 48000 voice.wav')
        with sr.AudioFile("voice.wav") as source:
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if assistant_name.lower() in command:
                command = command.replace("alexa ", '')
                display()

                print(f'COMMNAD: "{command}"\n')

                if 'go to' in command:
                    command = command.replace("go to ", "")
                    surf = f'surf {command}.com'
                    os.system(surf)
                elif 'say' in command:
                    command = command.replace('say ', '')
                    engine.say(command)
                    engine.runAndWait()
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


            else:
                display()
                print(f"You need to say my name, '{assistant_name}' in your commnad.")
                engine.say(f"You need to say my name, '{assistant_name}' in your commnad.")
                engine.runAndWait()
                main()
    except:
        print("Sorry, I didn't catch that... Please repeat that for me.")
        engine.say("Sorry, I didn't catch that... Please repeat that for me.")
        engine.runAndWait()
        main()

    # main()

main()

#===[ PROCESS THE COMMNAD ]===#
