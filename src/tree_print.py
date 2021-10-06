#!/usr/bin/python

import os


def tree_print():
    for root, dirs, files in os.walk('.'):
        path = root.split(os.sep)
        spaces = len(path) - 2

        if root != '.':
            print(spaces * '│   ' + '├──', os.path.basename(root))
            x = len(files)
            for i, file in enumerate(files):
                if i == (x-1):
                    print( (spaces + 1) * '│   ' + '└──', file)
                else:
                    print( (spaces + 1) * '│   ' + '├──', file)

        else :
            print(root)
            for file in files:
                print( (spaces + 1) * '│    ' + '├──', file)

tree_print()