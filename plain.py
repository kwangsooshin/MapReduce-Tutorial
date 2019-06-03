import sys

number_of_group = int(sys.stdin)
counter = [0 for x in range(number_of_group)]

for line in sys.stdin:
    group, number = line.split(",")
    group = int(group)
    number = float(number)

    if number >= counter[group]:
        counter[group] = number

for i in range(number_of_group):
    print("{},{}".format(i, counter[i]))

