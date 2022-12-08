with open("Day4.txt") as file:
    data = [i for i in file.read().splitlines()]

def part1(): 
    pairs = []

    for i in data:
        x = i.split(",")

        pairs.append(x)

    nissequeue = []

    for i in pairs:
        for j in i:
            x = j.split("-")

            specific_nisse = (int(x[0]), int(x[1]))


            nissequeue.append(specific_nisse)

    answer = 0

    for i in range(0, (len(nissequeue)-1), 2):
        specific_nisse = nissequeue[i]
        next_nisse = nissequeue[i+1]

        if (next_nisse[0] >= specific_nisse[0] and next_nisse[1] <= specific_nisse[1]) or (specific_nisse[0] >= next_nisse[0] and specific_nisse[1] <= next_nisse[1]):
            answer += 1
        
    return(answer)

print(part1())

def part2():
    pairs = []

    for i in data:
        x = i.split(",")

        pairs.append(x)

    nissequeue = []

    for i in pairs:
        for j in i:
            x = j.split("-")

            specific_nisse = (int(x[0]), int(x[1]))


            nissequeue.append(specific_nisse)

    answer = 0

    for i in range(0, (len(nissequeue)-1), 2):
        specific_nisse = nissequeue[i]
        next_nisse = nissequeue[i+1]

        if (specific_nisse[0] <= next_nisse[0] and specific_nisse[1] >= next_nisse[0] or specific_nisse[0] <= next_nisse[1] and specific_nisse[1] >= next_nisse[1]):
            answer += 1
        elif (next_nisse[0] <= specific_nisse[0] and next_nisse[1] >= specific_nisse[0] or next_nisse[0] <= specific_nisse[1] and next_nisse[1] >= specific_nisse[1]):
            answer += 1
        
    return(answer)

print(part2())