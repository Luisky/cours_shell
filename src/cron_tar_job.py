#!/usr/bin/python

from pathlib import Path
import subprocess

project_dir = str(Path.home()) + "/cours_shell"
res_dir = project_dir + "/resources/"
crontabak_path = "{}/crontab.bak".format(res_dir)

# we could also be using systemd timers and services : 
# https://dev.to/bowmanjd/schedule-jobs-with-systemd-timers-a-cron-alternative-15l8
# https://wiki.archlinux.org/title/Systemd/Timers#As_a_cron_replacement

# execution every two minutes : https://crontab.guru/#*/2_*_*_*_*
cron_seq = "*/2 * * * * {}/scripts/tar_archive.py".format(project_dir)
with open(crontabak_path) as f:
    f.write(cron_seq)

subprocess.run(["crontab", crontabak_path])