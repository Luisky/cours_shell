#!/usr/bin/python

import subprocess
import os

pids = {}

for i in range(0, 26):
    process = subprocess.Popen(["sleep", "1d"])
    pids[process.pid] = "running"

for i in range(0, 26):
    pid, status = os.wait()
    pids[pid] = "finished"

print(pids)
print("Good Job killing those sleepy jobs")