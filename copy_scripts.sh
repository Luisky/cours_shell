#!/bin/sh

# small script to copy my scripts : calls project.sh to generate the files
sh scripts/project.sh

cp "$(pwd)"/scripts/* scripts/.