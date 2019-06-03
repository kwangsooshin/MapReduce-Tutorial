import sys

for line in sys.stdin:
    group, number = line.split(',')
    print("{},{}".format(group, number))
