# f = open("inputTest2.txt", "r")
f = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""
# arr2d = [[j for j in i] for i in f.read().split("\n")]
arr2d = [[j for j in i] for i in f.split("\n")]
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


def areaSearch(pos, lastPos):
    if pos == (3,3):
        print(lastPos)
    #depth first search
    if min(pos) < 0 or pos[0] >= len(dotIntArr) or pos[1] >= len(dotIntArr[0]):
        return "O"
    
    if dotIntArr[pos[0]][pos[1]] == "I" or dotIntArr[pos[0]][pos[1]] == "O":
        # print("base")
        return dotIntArr[pos[0]][pos[1]]
    
    if pos[0] == lastPos[0]: 
        #moving horizontally
        if dotIntArr[pos[0]][pos[1]] == "|":
            return "I"
        elif dotIntArr[pos[0]][pos[1]] == ".":
            dotIntArr[pos[0]][pos[1]] = "I"

            returns = []
            returns.append(areaSearch((pos[0] + 1, pos[1]), pos) == "O")
            returns.append(areaSearch((pos[0] - 1, pos[1]), pos) == "O")
            returns.append(areaSearch((pos[0], pos[1] + 1), pos) == "O")
            returns.append(areaSearch((pos[0], pos[1] - 1), pos) == "O")
            if any(returns):
                dotIntArr[pos[0]][pos[1]] = "O"
                return "O"
            return "I"
        else:
            if lastPos[1] > pos[1]:
                return areaSearch((pos[0], pos[1] - 1), pos)
            else:
                return areaSearch((pos[0], pos[1] + 1), pos)
        
    elif pos[1] == lastPos[1]:
        #moving vertically
        if dotIntArr[pos[0]][pos[1]] == "-":
            return "I"
        elif dotIntArr[pos[0]][pos[1]] == ".":
            dotIntArr[pos[0]][pos[1]] = "I"

            returns = []
            returns.append(areaSearch((pos[0] + 1, pos[1]), pos) == "O")
            returns.append(areaSearch((pos[0] - 1, pos[1]), pos) == "O")
            returns.append(areaSearch((pos[0], pos[1] + 1), pos) == "O")
            returns.append(areaSearch((pos[0], pos[1] - 1), pos) == "O")
            if any(returns):
                dotIntArr[pos[0]][pos[1]] = "O"
                return "O"
            return "I"
        else:
            if lastPos[0] > pos[0]:
                return areaSearch((pos[0] - 1, pos[1]), pos)
            else:
                return areaSearch((pos[0] + 1, pos[1]), pos)
    else:
        print("AHHH")
    

# for i in range(len(arr2d)):
#     for j in range(len(arr2d[i])):
#         if arr2d[i][j] == ".":
#             areaSearchStart((i,j))

areaSearchStart((0,0))

for line in dotIntArr:
    print(line)