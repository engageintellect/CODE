#!/usr/bin/env bash

surf google.com & 

sleep 1

wm_id=$(wmctrl -l | grep surf | awk '{print $1}')





echo $wm_id
wmctrl -i -r $wm_id -e 0,333,115,1020,825
echo done
