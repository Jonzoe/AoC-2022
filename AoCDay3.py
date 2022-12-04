with open("Day3.txt") as file:
    data = [i for i in file.read().splitlines()]

def get_priority(x):
    return ord(x) - (96 if x.islower() else 38)

def part1():
    return sum(get_priority((set(x[:len(x)//2]) & set(x[len(x)//2:])).pop()) for x in data)

print(part1())

def part2():
    sum_pri = 0
    for x in range(0, len(data), 3):
        for i in data[x]:
            if i in data[x+1] and i in data[x+2]:
                sum_pri += (ord(i) - 96 if i.islower() else ord(i) - 38)
                break

    return(sum_pri)

print(part2())