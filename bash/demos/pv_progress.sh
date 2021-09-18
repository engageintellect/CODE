#!/usr/bin/env bash

while [ 0 ]; do 
    echo "test"
    sleep 0.005; 
done | pv > /dev/null
