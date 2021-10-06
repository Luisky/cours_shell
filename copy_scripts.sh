#!/bin/sh

# small script to copy my scripts : calls project.sh to generate the files

project_dir="${HOME}/cours_shell" #no space before or after the equal character
my_dir="${HOME}/Nextcloud/Cours ENSTA/cours_shell"

sh scripts/project.sh

cp "${my_dir}/scripts/"* scripts/.

