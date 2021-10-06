#!/bin/sh

if [ -z "$1" ]; then
    echo "Please provide one argument : the process name"
    exit
fi

kill -9 $(pgrep2 "$1")