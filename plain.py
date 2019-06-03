import sys

number_of_group = None
counter = None

for index, line in enumerate(sys.stdin):
    if index == 0:
        number_of_group = int(line)
        counter = [0 for x in range(number_of_group)]

    else:
        group, number = line.split(",")
        group = int(group)
        number = float(number)

        if number >= counter[group]:
            counter[group] = number

for i in range(number_of_group):
    print("{},{}".format(i, counter[i]))
