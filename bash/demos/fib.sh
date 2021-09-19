#!/bin/bash

# This program calculates the nth fibonacci number
#  using alrogirhtm 1A: naive binary recursion
#
# compiled: N/A
# executed: ./f1a.sh n
#

# Naive binary recursion: F(n) = F(n-1) + F(n-2)
fib () {
  if test $1 -lt 2; then
    echo $1
  else
    echo $(($(fib $(($1-2)))+$(fib $(($1-1)))))
  fi
}

# f handles the negative arguments: F(-n) = F(n)*(-1)^(n+1)
f () {
  if test $1 -lt 0; then
     if test $(($1%2)) -eq 0; then
         echo $((0-$(fib $((0-$1)))))
     else
         echo $(fib $((0-$1)))
     fi
  else
     echo $(fib $1)
  fi
}
# Function main checks the number of command line arguments, calls f()
# and prints the results
main () {
  if [ "$#" -ne 1 ]; then
      echo "Usage: $0 <n>"
  else
     RET=$(f $1)
     echo $1 "th Fibonacci number is" $RET
  fi
}
# entry point
main $1
