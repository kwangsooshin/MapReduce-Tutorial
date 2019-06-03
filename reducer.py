import sys

data = {}

for line in sys.stdin:
    (group, number) = line.split(",")

    if group in data.keys():
        data[group] = max(data[group], number)
    else:
        data[group] = number

for group, number in data.items():
    print("{},{}".format(group, number))
