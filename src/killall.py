#!/usr/bin/python

import argparse
import psutil


def pgrep(process_name : str):
    ret = []
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if process_name in p.name():
            ret.append(pid)
    return ret


parser = argparse.ArgumentParser(description='kill processes with the name given as arguments')
parser.add_argument('process_name', type=str, help='the process name')
args = parser.parse_args()

pids = pgrep(args.process_name)
for pid in pids:
    p = psutil.Process(pid)
    p.kill()