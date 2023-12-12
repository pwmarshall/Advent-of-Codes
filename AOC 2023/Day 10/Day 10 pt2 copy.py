f = open("inputTest2.txt", "r")
# f = """..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# .........."""
arr2d = [[j for j in i] for i in f.read().split("\n")]
# arr2d = [[j for j in i] for i in f.split("\n")]
print(arr2d)

arr2dCopy = [[j for j in i] for i in arr2d]
pathPos = []

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
        pathPos.append(pos)

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

print()
dotIntArr = [["." if (i,j) not in pathPos else arr2dCopy[i][j] for j in range(len(arr2d[i]))] for i in range(len(arr2d))]

for line in dotIntArr:
    print(line)

def areaSearchStart(start):

    areaSearch((start[0] + 1, start[1]), start)
    areaSearch((start[0] - 1, start[1]), start)
    areaSearch((start[0], start[1] + 1), start)
    areaSearch((start[0], start[1] - 1), start)


def areaSearch(start):
    queue = []
    queueLast = []
    outside = False

    queue.append((start[0] + 1, start[1]))
    queueLast.append(start)
    queue.append((start[0] - 1, start[1]))
    queueLast.append(start)
    queue.append((start[0], start[1] + 1))
    queueLast.append(start)
    queue.append((start[0], start[1] - 1))
    queueLast.append(start)

    while (len(queue) != 0):
        pos = queue.pop(0)
        lastPos = queueLast.pop(0)

        #breath first search
        if min(pos) < 0 or pos[0] >= len(dotIntArr) or pos[1] >= len(dotIntArr[0]):
            outside = True
            continue
        
        if dotIntArr[pos[0]][pos[1]] == "I" and outside:
            dotIntArr[pos[0]][pos[1]] = "O"
            queue.append((pos[0] + 1, pos[1]))
            queueLast.append(pos)
            queue.append((pos[0] - 1, pos[1]))
            queueLast.append(pos)
            queue.append((pos[0], pos[1] + 1))
            queueLast.append(pos)
            queue.append((pos[0], pos[1] - 1))
            queueLast.append(pos)
        elif dotIntArr[pos[0]][pos[1]] == "I" or dotIntArr[pos[0]][pos[1]] == "O":
            continue
        
        if pos[0] == lastPos[0]: 
            #moving horizontally
            if dotIntArr[pos[0]][pos[1]] == "|":
                continue
            elif dotIntArr[pos[0]][pos[1]] == ".":
                if outside:
                    dotIntArr[pos[0]][pos[1]] = "O"
                else:
                    dotIntArr[pos[0]][pos[1]] = "I"

                returns = []

                if pos[0] + 1 < len(dotIntArr):
                    queue.append((pos[0] + 1, pos[1]))
                    queueLast.append(pos)
                else:
                    outside = True

                if pos[0] - 1 >= 0:
                    queue.append((pos[0] - 1, pos[1]))
                    queueLast.append(pos)
                else:
                    outside = True

                if pos[1] + 1 < len(dotIntArr[0]):
                    queue.append((pos[0], pos[1] + 1))
                    queueLast.append(pos)
                else:
                    outside = True

                if pos[1] - 1 >= 0:
                    queue.append((pos[0], pos[1] - 1))
                    queueLast.append(pos)
                else:
                    outside = True

            else:
                if lastPos[1] > pos[1]:
                    queue.append((pos[0], pos[1] - 1))
                    queueLast.append(pos)
                else:
                    queue.append((pos[0], pos[1] + 1))
                    queueLast.append(pos)
            
        elif pos[1] == lastPos[1]:
            #moving vertically
            if dotIntArr[pos[0]][pos[1]] == "-":
                continue
            elif dotIntArr[pos[0]][pos[1]] == ".":
                if outside:
                    dotIntArr[pos[0]][pos[1]] = "O"
                else:
                    dotIntArr[pos[0]][pos[1]] = "I"

                returns = []

                if pos[0] + 1 < len(dotIntArr):
                    queue.append((pos[0] + 1, pos[1]))
                    queueLast.append(pos)
                else:
                    outside = True

                if pos[0] - 1 >= 0:
                    queue.append((pos[0] - 1, pos[1]))
                    queueLast.append(pos)
                else:
                    outside = True

                if pos[1] + 1 < len(dotIntArr[0]):
                    queue.append((pos[0], pos[1] + 1))
                    queueLast.append(pos)
                else:
                    outside = True

                if pos[1] - 1 >= 0:
                    queue.append((pos[0], pos[1] - 1))
                    queueLast.append(pos)
                else:
                    outside = True

            else:
                if lastPos[0] > pos[0]:
                    queue.append((pos[0] - 1, pos[1]))
                    queueLast.append(pos)
                else:
                    queue.append((pos[0] + 1, pos[1]))
                    queueLast.append(pos)

        else:
            print("AHHH")
    

for i in range(len(arr2d)):
    for j in range(len(arr2d[i])):
        if arr2d[i][j] == ".":
            areaSearch((i,j))

# areaSearch((0,0))

for line in dotIntArr:
    print(line)


# print(sum([1 for i in j for j in dotIntArr if i == "I"]))

sum = 0

for line in dotIntArr:
    for space in line:
        if space == "I":
            sum += 1

print(sum)