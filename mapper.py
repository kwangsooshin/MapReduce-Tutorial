import sys

for index, line in enumerate(sys.stdin):
    if index != 0:
        group, number = line.strip().split(",")
        print("{},{}".format(group, number))
