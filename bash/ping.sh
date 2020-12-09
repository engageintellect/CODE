#!/usr/bin/env bash


ping_cmd=$(ping -c 1 google.com)

echo $ping_cmd > ping.txt

p_out=$(awk '{print $14}' ping.txt | sed 's/time=//')
rm -rf ping.txt

echo ping $p_out ms 









