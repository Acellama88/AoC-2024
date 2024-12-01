import re

left = []
right = []
total = 0

with open("input.txt", "r") as f:
    for line in f:
        arr = list(filter(None, re.split(" |\n", line)))
        left.append(int(arr[0]))
        right.append(int(arr[1]))
    left.sort()
    right.sort()
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    print(f"Part1: {total}")

    total = 0
    last = None
    lastScore = 0
    for i in range(len(left)):
        if(left[i] == last):
            total += lastScore
            continue
        else:
            occurs = right.count(left[i])
            score = occurs * left[i]
            last = left[i]
            lastScore = score
            total += score
    print(f"Part2: {total}")