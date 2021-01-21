#!/usr/bin/env bash


updates=$(sudo pacman -Syu | grep -w Packages | awk '{print $2}' | sed 's/(//g' | sed 's/)//g')


if [[ $packages == "" ]]; then 
    updates=0
    echo UPDATES: $updates
else
    echo UPDATES: $packages
fi
