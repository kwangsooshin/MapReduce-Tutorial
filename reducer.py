#!/usr/bin/env python

import sys

data = {}

for index, line in enumerate(sys.stdin):
    group, number = line.strip().split("\t")
    number = float(number)

    if group in data.keys():
        data[group] = max(data[group], number)
    else:
        data[group] = number

for group, number in data.items():
    print("%s\t%s" % (group, number))
