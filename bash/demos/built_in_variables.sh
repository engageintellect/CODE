#!/usr/bin/env bash

# to run this script use "source {path/to/script.sh}; {function_name} arg1 arg2 arg3 etc...

tester() {
    echo "$@ is" $@
    echo "$1 is" $1
    echo "$2 is" $2
    echo "$# is" $#
    echo "$* is" $*
    echo "$_ is" $_
}
