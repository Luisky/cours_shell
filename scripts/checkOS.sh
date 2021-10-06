#!/bin/sh

checkOS()
{
    os="unknown"
    x=$(uname | tr '[:upper:]' '[:lower:]')
    case "${x}" in 
        darwin*) os="osx" ;;
        linux*) os="linux" ;;
        mssys* | cygwin*) os="windows" ;;
        *bsd) os="bsd";;
    esac
    echo "This os is $os"
}

checkOS