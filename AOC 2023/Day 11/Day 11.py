import math

f = open("inputTest.txt", "r")
lines = f.read().split("\n")
print(lines)
for line in lines:
    print(line)

# linesToExpand = [i if "#" not in lines[i] else -1 for i in range(len(lines))]

rowsToExpand = []
columnsToExpand = []

for i in range(len(lines)):
    if "#" not in lines[i]:
        rowsToExpand.append(i)

for i in range(len(lines[0])):
    if "#" not in [lines[j][i] for j in range(len(lines[0]))]:
        columnsToExpand.append(i)

print(rowsToExpand, columnsToExpand)

expandedUniverse = []
expandFactor = 2 #replace empty row with x number

for i in range(len(lines)): #rows
    if i in rowsToExpand:
        for j in range(expandFactor):
            expandedUniverse.append("." * (len(lines[0]) + len(columnsToExpand)*(expandFactor-1)))
        continue

    line = ""
    for j in range(len(lines[0])): # columns
        if j in columnsToExpand:
            line += ("." * (expandFactor-1))
        line += lines[i][j]

    expandedUniverse.append(line)

for line in expandedUniverse:
    print(line)

stars = []

for i in range(len(expandedUniverse)): #rows
    for j in range(len(expandedUniverse[0])): # columns
        if expandedUniverse[i][j] == "#":
            stars.append((i,j))

print(stars)

sumDistance = 0

for i in range(len(stars)-1):
    for j in range(i+1, len(stars)):
        pos1 = stars[i]
        pos2 = stars[j]
        sumDistance += math.fabs(pos1[0] - pos2[0]) + math.fabs(pos1[1] - pos2[1])

print(sumDistance)