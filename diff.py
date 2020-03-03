#!/usr/bin/env python


import difflib, sys

with open ("file1.txt", "r") as file1:
    dataset1=file1.readlines()

with open ("file2.txt", "r") as file2:
    dataset1=file2.readlines()

for line in difflib.context_diff(file1, file2):
    sys.stdout.write(line)