f = open("inputTest.txt", "r")
arr2d = [[j for j in i] for i in f.read().split("\n")]
print(arr2d)

start = (index := max([i for i in range(len(arr2d)) if "S" in arr2d[i]]), arr2d[index].index("S"))

print(start)

def searchCorrect(start):
    queue = []

    queue.append(start)
    count = 0

    while len(queue) != 0:
        pos = queue.pop(0)
        # print(f"Searching {pos}")

        if isinstance(arr2d[pos[0]][pos[1]], int):
            continue

        pipe = arr2d[pos[0]][pos[1]]
        arr2d[pos[0]][pos[1]] = int(count)

        if pipe == "|":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0] - 1, pos[1]))
            count += 0.5
        elif pipe == "-":
            queue.append((pos[0], pos[1] + 1))
            queue.append((pos[0], pos[1] - 1))
            count += 0.5
        elif pipe == "L":
            queue.append((pos[0] - 1, pos[1]))
            queue.append((pos[0], pos[1] + 1))
            count += 0.5
        elif pipe == "J":
            queue.append((pos[0] - 1, pos[1]))
            queue.append((pos[0], pos[1] - 1))
            count += 0.5
        elif pipe == "7":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0], pos[1] - 1))
            count += 0.5
        elif pipe == "F":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0], pos[1] + 1))
            count += 0.5
        elif pipe == "S":
            if (next := arr2d[pos[0] - 1][pos[1]]) == "|" or next == "7" or next == "F":
                queue.append((pos[0] - 1, pos[1]))
            if (next := arr2d[pos[0] + 1][pos[1]]) == "|" or next == "L" or next == "J":
                queue.append((pos[0] + 1, pos[1]))
            if (next := arr2d[pos[0]][pos[1] - 1]) == "-" or next == "L" or next == "F":
                queue.append((pos[0], pos[1] - 1))
            if (next := arr2d[pos[0]][pos[1] + 1]) == "-" or next == "7" or next == "J":
                queue.append((pos[0], pos[1] + 1))
            
            count += 1


    return int(count)


print(searchCorrect(start))

for line in arr2d:
    print(line)