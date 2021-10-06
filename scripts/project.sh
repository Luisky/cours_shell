#!/bin/sh

project_dir="${HOME}/cours_shell" #no space before or after the equal character

mkdir -p "$project_dir"
cd "$project_dir" || exit
echo "This script will execute in this directory : $(pwd)"

touch compte_rendu.txt
mkdir -p archives
mkdir -p bin
mkdir -p resources
mkdir -p scripts
touch scripts/checkOS.sh
touch scripts/cron_tar_job.sh
touch scripts/killall.sh
touch scripts/project.sh
touch scripts/pgrep.sh
touch scripts/source.sh
touch scripts/spawn_procs.sh
touch scripts/tar_archive.sh
touch scripts/tree_print.sh

chmod -R u+rwX,go-rwX .
chmod -R u+x scripts/