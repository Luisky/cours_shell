#!/bin/sh

# https://www.shellcheck.net/wiki/SC2009 -- Consider using pgrep instead of grepping ps output.
# Thanks ShellCheck, but that's the entire point of this challenge !

if [ -z "$1" ]; then
    echo "Please provide one argument : the process name"
    exit
fi

ps -aux | grep "$1" | grep -v "grep" | awk '{print $2}'