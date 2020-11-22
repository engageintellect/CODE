#!/usr/bin/env bash

. "${HOME}/.cache/wal/colors.sh"


declare options=("bspwm_reload
logout
restart
shutdown
quit")

choice=$( echo -e "${options[0]}" | dmenu -fn 'Hack Nerd font -9' -nb "$color0" \
    -nf "$color15" -sb "$color3" -sf "$color0" -h 25 -p 'SESSION:')

case "$choice" in
    quit)
        echo "program terminated." && exit 1
    ;;
    bspwm_reload)
        bspc wm -r
    ;;
    logout)
        killall bspwm
    ;;
    restart)
        sudo reboot
    ;;
    shutdown)
        echo sudo shutdown now
    ;;
    *)
        exit 1
    ;;
esac

