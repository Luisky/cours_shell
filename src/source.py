#!/usr/bin/python

from pathlib import Path
import os

project_dir = str(Path.home()) + "/cours_shell"
scripts_dir = project_dir + "/scripts/"
bin_dir = project_dir + "/bin/"

def ln_script_to_bin(src, dst):
    os.symlink(scripts_dir + src, bin_dir + dst)


ln_script_to_bin("pgrep.sh", "pgrep2")
ln_script_to_bin("killall.sh", "killall2")
ln_script_to_bin("spawn_procs.sh", "spawn_procs")

# la partie export ne marcherait pas a cause du fork fait par le shell
# donc ecrire un script comme celui la :
# #!/bin/sh
# export PATH="${project_dir}/bin:$PATH" 