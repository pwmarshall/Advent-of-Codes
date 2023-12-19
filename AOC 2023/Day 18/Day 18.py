f = open("input.txt", "r")
intructions = [i for i in f.read().split("\n")]

print(intructions)


digPlan = [["*"]]
currentPos = [0,0]

for intruct in intructions:
    direction, length, color = intruct.split(" ")

    length = int(length)
    # color deal with later

    if direction == "U":
        direction = [-1,0]
    elif direction == "R":
        direction = [0,1]
    elif direction == "D":
        direction = [1,0]
    elif direction == "L":
        direction = [0,-1]
    else:
        print("No")

    
    for i in range(length):
        newPos = [sum(i for i in j) for j in zip(currentPos, direction)]
        if newPos[0] < 0:
            newPos[0] += 1
            digPlan.insert(0, ["." for j in range(len(digPlan[0]))])
        elif newPos[0] >= len(digPlan):
            # newPos[0] += 1
            digPlan.append(["." for j in range(len(digPlan[0]))])
        elif newPos[1] < 0:
            newPos[1] += 1
            [digPlan[j].insert(0, ".") for j in range(len(digPlan))]
        elif newPos[1] >= len(digPlan[0]):
            # newPos[1] += 1
            [digPlan[j].append(".") for j in range(len(digPlan))]
        
        if digPlan[newPos[0]][newPos[1]] != "*":
            digPlan[newPos[0]][newPos[1]] = "#"

        currentPos = newPos
    

# print(digPlan)

o = open("output.txt", "w")
startPos = [-1,-1]

for line in digPlan:
    o.write("".join(line) + "\n")
    if "*" in line:
        startPos = [digPlan.index(line), line.index("*")]


queue = []
if startPos == [-1, -1]:
    print("start pos not found")
queue.append([startPos[0] + 1, startPos[1] + 1])

while len(queue) > 0:
    pos = queue.pop(0)

    digPlan[pos[0]][pos[1]] = "#"
    for delta in [[-1,0], [1,0], [0,-1], [0, 1]]:
        newPos = [sum(i for i in j) for j in zip(pos, delta)]
        if digPlan[newPos[0]][newPos[1]] != "#":
            queue.append(newPos)

o = open("outputFill.txt", "w")
for line in digPlan:
    o.write("".join(line) + "\n")


