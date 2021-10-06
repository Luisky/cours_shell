#!/usr/bin/python

from pathlib import Path
import subprocess
import os
import datetime
import tarfile


project_dir = str(Path.home()) + "/cours_shell"
old_state_path = project_dir + "/resources/old_state"
cur_state_path = project_dir + "/resources/cur_state"
scripts_path = project_dir + "/scripts/"

with open(cur_state_path, 'w') as f:
  subprocess.run(["ls", "-al", scripts_path], stdout=f)

if os.path.exists(old_state_path):
  print("old metadata found")
else:
  open(old_state_path, 'w').close()

ret = subprocess.run(["diff", cur_state_path, old_state_path]).returncode

if ret == 0:
  print("nothing to do")
elif ret == 1:
  now = datetime.date.strftime("%Y%m%d-%H%M%S")
  tar_path = project_dir + "/archives/src_" + now + ".tar.gz"
  tar_file = tarfile.open(tar_path, 'w|gz')
  for root, dirs, files in os.walk(scripts_path):
    for filename in files:
      tar_file.addfile(filename)
else:
  print("error with diff")

subprocess.run(["cp", cur_state_path, old_state_path])
