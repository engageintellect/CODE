#!/usr/bin/env bash

    
main(){
    clear
    updates=$(sudo pacman -Syu | grep -w Package | awk '{print $2}' | sed 's/(//g' | sed 's/)//g')


    if [[ $updates=="" ]]; then 
        updates=0
    else
        continue
    fi

    echo AVAILABLE UPDATES: $updates

}

main
