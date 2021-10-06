#!/bin/sh

project_dir="${HOME}/cours_shell" #no space before or after the equal character
old_state_path="${project_dir}/resources/old_state"
cur_state_path="${project_dir}/resources/cur_state"
scripts_path="${project_dir}/scripts/"
ls -al "$scripts_path" > "$cur_state_path"

if test -f "$old_state_path"; then
  echo "old metadata found"
else
  touch "$old_state_path"
fi

diff "$cur_state_path" "$old_state_path" > /dev/null 2>&1
ret=$?

if [ $ret -eq 0 ]; then
  echo "nothing to do"
elif [ $ret -eq 1 ]; then
  now=$(date +'%d-%m-%Y_%H-%M-%S')
  tar -czf "${project_dir}/archives/scripts_$now.tar.gz" -C "$scripts_path"
else
  echo "error"
fi

cp "$cur_state_path" "$old_state_path"
