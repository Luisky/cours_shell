#!/bin/sh

project_dir="${HOME}/cours_shell" #no space before or after the equal character
res_dir="${project_dir}/resources/"

# we could also be using systemd timers and services : 
# https://dev.to/bowmanjd/schedule-jobs-with-systemd-timers-a-cron-alternative-15l8
# https://wiki.archlinux.org/title/Systemd/Timers#As_a_cron_replacement


# execution every two minutes : https://crontab.guru/#*/2_*_*_*_*
cron_seq="*/2 * * * * ${project_dir}/scripts/tar_archive.sh"
echo "$cron_seq" > "${res_dir}/crontab.bak"
crontab "${res_dir}/crontab.bak"