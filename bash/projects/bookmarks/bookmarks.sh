#!/usr/bin/env bash


bookmarks=$(cat ~/bin/bookmarks.txt)


read selection <<< $(for x in $bookmarks; do echo $x; done | rofi -dmenu)


if [[ $selection == "" ]]; then
    echo nothing selected, exiting...
else
    surf $selection
fi

done



