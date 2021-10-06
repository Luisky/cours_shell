#!/usr/bin/python

from pathlib import Path
import os
import subprocess

project_dir = str(Path.home()) + "/cours_shell"
if not os.path.exists(project_dir):
    os.mkdir(project_dir)
os.chdir(project_dir)
print(project_dir)


Path('compte_rendu.txt').touch()
dirs = ['archives', 'bin', 'resources', 'scripts', 'src']
for d in dirs:
    if not os.path.exists(d):
        os.mkdir(d)

scripts = ['checkOS', 'cron_tar_job', 'killall', 'project', 'pgrep', 'source', 'spawn_procs', 'tar_archive', 'tree_print']
for s in scripts:
    sp = 'src/{}.py'.format(s)
    if not os.path.exists(sp):
        open(sp, 'w').close()

subprocess.run(["chmod", "-R", "u+rwX,go-rwX", "."])
subprocess.run(["chmod", "-R", "u+x", "src/"])