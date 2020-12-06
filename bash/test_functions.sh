#!/bin/bash

function talk {
    echo "$@ is" $@
    echo "$1 is" $1
    echo "$2 is" $3
    echo "$# is" $#
    echo "$? is" $?

}


function ask {
    echo hello
    echo -n "what is your name?: "; read name;
    echo hello $name
}



