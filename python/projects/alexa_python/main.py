#!/usr/bin/env python3

import os
import subprocess
from time import sleep
import speech_recognition as sr


#===[ INITIALIZE LISTENER ]===#
listener = sr.Recognizer()


def display():
    os.system('clear'); os.system('figlet jiggz'); print('\n')

def clear_screen():
    os.system('clear')



##==[ LISTEN WITH MICROPHONE (NOT WORKING) ]==#
#try:
#    with sr.Microphone(device_index=0) as source:
#        voice = listener.listen(source)
#        command = listener.recognize_google(voice)
#        print(command)
#except:
#    print("Sorry, I didn't get that... Please repeat that for me.")
#    pass


#===[ RECORD VOICE TO FILE (MICROPHONE WORKAROUND) ]===#

try:
    display()
    print('Listening...\n')
    os.system('arecord -d 4 --device hw:0,0 --format s16_le --channels 2 --rate 48000 voice.wav')
    with sr.AudioFile("voice.wav") as source:
        audio = listener.listen(source)
        command = listener.recognize_google(audio)
        display()
        print(command, '\n')
except:
    print("Sorry, I didn't get that... Please repeat that for me.")
    pass



#===[ PROCESS THE COMMNAD ]===#
