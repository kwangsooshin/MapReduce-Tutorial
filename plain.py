with open("input.data", "r") as f:
    number_of_group = int(f.readline())

    counter = [0 for x in range(number_of_group)]

    for line in f:
        group, number = line.split(",")
        group = int(group)
        number = float(number)

        if number >= counter[group]:
            counter[group] = number

    for i in range(number_of_group):
        print("{},{}".format(i, counter[i]))

