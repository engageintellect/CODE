#!/bin/bash


progress()
{
    echo -n "["
    for ((i = 0 ; i <= 100 ; i+=6)); do
        sleep 0.05
        echo -n "###"
    done
    echo -n "]"
    echo
}


progress
