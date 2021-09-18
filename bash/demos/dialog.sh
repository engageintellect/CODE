#!/usr/bin/env bash

dialog --title 'Message' --msgbox 'Hello, world!' 5 20

dialog --title "Message"  --yesno "Are you having\ fun?" 6 25

dialog --infobox "Please wait" 10 30 ; sleep 4

dialog --inputbox "Enter your name:" 8 40 2>/dev/null

