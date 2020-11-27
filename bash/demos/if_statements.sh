#!/usr/bin/env bash


# question 1
echo -n "what is your name?: "; read name; 

if [[ $name != "josh" ]]; then
    echo "your name is not josh"
else
    echo "your name is josh"
fi



# question 2
echo -n "enter your age: "; read age;


if [[ $age > 21 ]]; then
    echo "you are old enough to drink"
else
    echo "you are not old enough to drink"
fi



# which one is greater?
echo -n "pick a number: "; read num1; 
echo -n "pick another number: "; read num2; 

if [[ $num1 > $num2 ]]; then
    echo $num1 is greater than $num2
else
    echo $num2 is greater than $num1
fi




