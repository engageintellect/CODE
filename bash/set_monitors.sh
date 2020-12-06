#!/usr/bin/env bash

# CHECK XRANDR FOR CONNECTED MONITORS
clear; echo "===[ CONNECTED MONITORS ]==="; echo ""
xrandr -q | grep --color=auto -w connected; sleep 2

# ASSIGN CONNECTED MONITOS TO VARIABLE
connected_monitors=$(xrandr -q | grep -w connected)


# DECIDE WHICH MONITOR SCRIPT TO RUN
if [[ "$connected_monitors" == *"VGA"* ]]; then 
    echo ""; echo -n "External monitors are connected, would you like to apply corresponding layout? [Y/n]: "; read apply
    if [[ $apply != *"n"* ]]; then
        echo ""; echo "Applying horizontal_layout script..."; sleep .5
        ~/bin/env/display_settings/dual_displays.sh
        bspc wm -r
        bspc desktop -f '^2'
        echo ""
        echo "Layout set successfully"; sleep 1; echo "Exiting..."; sleep 1; clear
        killall st
    else
        echo "sounds good, later..."; sleep 1; clear
    fi
else
    echo "No external monitors detected, applying default layout."; sleep 1;
    ~/bin/env/display_settings/laptop_mode.sh
    clear
fi

exit











