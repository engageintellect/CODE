#!/usr/bin/env bash


function list {

    likes=("pizza" 
        "icecream" 
        "turkey" 
        "soup" 
        "sandwiches")

    dislikes=("mushrooms" 
        "anchovies" 
        "barf" 
        "soggy" 
        "crap")

    
    for i in $likes; do
        echo you like $i
    done

    
    for i in $dislikes; do
        echo you dont like $i
    done

}





function cheater {

    clear
    if [ "$1" = "" ]; then 
        echo -n "enter a command to search: "; read command
        if [ $command = "q" ]; then
            echo "Terminating Program"
            sleep 1
            clear
        else
            curl cheat.sh/$command
        fi
    else curl cheat.sh/$1
    fi

}


function sayhi {

    echo -n "what is your name?: "; read name; echo "hello $name!";

}


function updater {

    echo -n "are you ready to run an update?: "; read ready;
    if [ $ready = "y" ]; then 
        sudo pacman -Syu
    else
        echo "Program Terminated"
        exit
    fi

}



