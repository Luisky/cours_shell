#!/bin/sh

project_dir="${HOME}/cours_shell" #no space before or after the equal character

ln_script_to_bin()
{
    ln -s "${project_dir}/scripts/$1" "${project_dir}/bin/$2"
}

ln_script_to_bin "pgrep.sh" "pgrep2"
ln_script_to_bin "killall.sh" "killall2"
ln_script_to_bin "spawn_procs.sh" "spawn_procs"

export PATH="${project_dir}/bin:$PATH"