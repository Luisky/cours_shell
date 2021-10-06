#!/bin/sh

# small script to copy my scripts : calls project.sh to generate the files

project_dir="${HOME}/cours_shell" #no space before or after the equal character

sh scripts/project.sh

cp "$(pwd)"/scripts/* "${project_dir}"/scripts/.

