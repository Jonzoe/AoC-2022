#Läser textfilen
with open("Day1.txt") as file:
    data = [[int(i) for i in x.splitlines()] for x in file.read().split("\n\n")]

sorted_data = sorted(sum(x) for x in data)

def part1():
    return (max(sorted_data))

def part2():
    return (sum(sorted_data[-3:]))

print(part1())
print(part2())