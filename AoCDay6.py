with open("Day6.txt") as file:
    data = file.read()

def part1():

    four = []

    for x in data:
        four.append(x)
        if len(four) > 4:
            set_of_four = set(four[-5:-1])
            if len(set_of_four) == 4:
                return (len(four)-1)

print(part1())

def part2():
    fourteen = []

    for x in data:
        fourteen.append(x)
        if len(fourteen) > 14:
            set_of_four = set(fourteen[-15:-1])
            if len(set_of_four) == 14:
                return (len(fourteen)-1)

print(part2())