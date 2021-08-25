#!/usr/bin/env bash


clear_screen()
{
    clear && figlet "XMRIG"
}



record_screen()
{
    res=$(xrandr | grep connected | grep primary | awk '{print $4}' | sed "s/+0+0//g")
    echo -n "ENTER FILE NAME: "
    read filename

    if [[ $filename == "q" ]]; then
        clear && exit
    else
        cd
        ffmpeg -f x11grab -s $res -r 25 -i :0.0 $filename.mp4
        clear && echo "SAVING VIDEO '$filename'" && sleep 1
        clear
    fi
}


clear_screen
record_screen
