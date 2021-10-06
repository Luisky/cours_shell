#!/usr/bin/python

from pathlib import Path
import subprocess
import os
from datetime import datetime


project_dir = str(Path.home()) + "/cours_shell"
old_state_path = project_dir + "/resources/old_state"
cur_state_path = project_dir + "/resources/cur_state"
src_path = project_dir + "/src/"

with open(cur_state_path, 'w') as f:
  subprocess.run(["ls", "-al", src_path], stdout=f)

if os.path.exists(old_state_path):
  print("old metadata found")
else:
  open(old_state_path, 'w').close()

with open('/dev/null', 'w') as f:
  ret = subprocess.run(["diff", cur_state_path, old_state_path], stdout=f).returncode

if ret == 0:
  print("nothing to do")
elif ret == 1:
  now = datetime.now()  
  now_str = now.strftime('%Y%m%d-%H%M%S')
  tar_path = project_dir + "/archives/src_" + now_str + ".tar.gz"
  print(tar_path)
  # I could use import tarfile and its api but it's simpler like that
  os.chdir(src_path)
  subprocess.run(["tar", "-czf", tar_path, '.'])
else:
  print("error with diff")

subprocess.run(["cp", cur_state_path, old_state_path])
