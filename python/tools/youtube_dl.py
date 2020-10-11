import os
import subprocess
import time

# set download folder/path
def set_folder():
    # get username
    usr = os.getcwd()
    usr = usr.replace("/home/", "")
    
    # make download folder is not there already.
    path = os.listdir()
    if 'videos' in path:
        os.chdir('videos')
        a = os.listdir()
        if 'youtube' in a:
            main()
        else:
            os.mkdir('youtube')
            main()
    else:
        os.chdir('/home/' + usr)
        os.mkdir('videos')
        os.chdir('videos')
        os.mkdir('youtube')
        main()

# main program
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
                os.chdir('/home/r3dux/videos/.porn/')
            else:
                os.chdir('/home/r3dux/videos/youtube/')
            print('\n')

            # download video
            os.system('youtube-dl ' + str(usr_input) + ' -o ' + str(output_file))
            print('\n')
            print('VIDEO DOWNLOAD COMPLETE')
            time.sleep(2)
            os.system('clear')
            main()

set_folder()
