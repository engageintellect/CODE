import os
import subprocess
import time

def set_folder():
    usr = os.getcwd()
    usr = usr.replace("/home/", "")
    path = os.listdir()
    if 'media' in path:
        os.chdir('media')
        path = os.listdir()
        if 'videos' in path:
            os.chdir('videos')
            path = os.listdir()
            if 'youtube' in path:
                main()
            else:
                os.mkdir('youtube')
        else:
            os.mkdir('videos')
            os.chdir('videos')
            os.mkdir('youtube')
            main()
    else:
        os.chdir('/home/' + usr)
        os.mkdir('media')
        os.chdir('media')
        os.mkdir('videos')
        os.chdir('videos')
        os.mkdir('youtube')
        os.chdir('youtube')
        main()

def main():
    os.system('clear')
    print("                   _         _                    _ _")
    print(" _   _  ___  _   _| |_ _   _| |__   ___        __| | |")
    print("| | | |/ _ \| | | | __| | | | '_ \ / _ \_____ / _` | |")
    print("| |_| | (_) | |_| | |_| |_| | |_) |  __/_____| (_| | |")
    print(" \__, |\___/ \__,_|\__|\__,_|_.__/ \___|      \__,_|_|")
    print(" |___/")
    print('\n')

    # user input
    usr_input = input('ENTER URL: ')

    if usr_input == 'q':
        os.system('clear')
        quit()
    else:
        output_file = input('ENTER A NAME FOR FILE: ')
        if output_file == 'q':
            os.system('clear')
            quit()
        else:
            file_type = input('VIDEO TYPE: ')
            if file_type == 'q':
                os.system('clear')
                quit()
            if file_type == 'porn':
                os.chdir('/home/r3dux/media/videos/')
                path = os.listdir()
                if '.porn' in path:
                    os.chdir('/home/r3dux/media/videos/.porn/')
                else:
                    os.mkdir('.porn')
                    os.chdir('/home/r3dux/media/videos/.porn/')
            else:
                os.chdir('youtube')
            
            print('\n')

            # download video
            os.system('youtube-dl ' + str(usr_input) + ' -o ' + str(output_file))
            print('\n')
            print('VIDEO DOWNLOAD COMPLETE')
            time.sleep(2)
            os.system('clear')
            main()

set_folder()
