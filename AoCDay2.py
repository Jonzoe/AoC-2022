with open("Day2.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

def part1():

    points = 0

    for tjofräs in data:

        if (tjofräs == "A X"):
            points += 4

        if (tjofräs == "A Y"):
            points += 8

        if (tjofräs == "A Z"):
            points += 3

        if (tjofräs == "B X"):
            points += 1

        if (tjofräs == "B Y"):
            points += 5

        if (tjofräs == "B Z"):
            points += 9

        if (tjofräs == "C X"):
            points += 7

        if (tjofräs == "C Y"):
            points += 2

        if (tjofräs == "C Z"):
            points += 6

    return(points)

def part2():
    
    points = 0

    for tjofräs in data:
        if (tjofräs == "A X"):
            points += 3

        if (tjofräs == "A Y"):
            points += 4

        if (tjofräs == "A Z"):
            points += 8

        if (tjofräs == "B X"):
            points += 1

        if (tjofräs == "B Y"):
            points += 5

        if (tjofräs == "B Z"):
            points += 9

        if (tjofräs == "C X"):
            points += 2

        if (tjofräs == "C Y"):
            points += 6

        if (tjofräs == "C Z"):
            points += 7

    return(points)

print(part1())
print(part2())