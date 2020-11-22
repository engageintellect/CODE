#!/usr/bin/env bash


echo ==[ SURFER ]==

echo -n "ENTER A URL: "; read url; 

if [ $url == "q" ]; then echo "Program Terminated" && clear && exit 1; else surf $url; fi
