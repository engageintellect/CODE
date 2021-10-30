#!/usr/bin/env bash

gtts-cli "hello world" --output ~/output.mp3
mpv ~/output.mp3 &
sudo rm -rf ~/output.mp3

