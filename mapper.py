#!/usr/bin/env python

import sys

for index, line in enumerate(sys.stdin):
    group, number = line.strip().split(",")
    print("%s\t%s" % (group, number))
