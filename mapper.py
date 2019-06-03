import sys

for index, line in enumerate(sys.stdin):
    group, number = line.strip().split(",")
    print("{},{}".format(group, number))
