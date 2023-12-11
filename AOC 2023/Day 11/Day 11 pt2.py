f = open("inputTest.txt", "r")
lines = f.read().split("\n")
print(lines)

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

expandFactor = 100 #replace empty row with x number

stars = [] #pos before expansion

for i in range(len(lines)): #rows
    for j in range(len(lines[0])): # columns
        if lines[i][j] == "#":
            stars.append((i,j))

print(stars)

newStars = []
index = 0

for i in range(len(stars)): # transform rows 
    if index < len(rowsToExpand) and stars[i][0] > rowsToExpand[index]:
        index += 1
    newStars.append((stars[i][0] + index*(expandFactor-1), stars[i][1]))

# print(newStars)

newStars.sort(key=lambda a: a[1])

# print(newStars)

newNewStars = []
index = 0

for i in range(len(newStars)): # transform columns 
    if index < len(columnsToExpand) and newStars[i][1] > columnsToExpand[index]:
        index += 1
    newNewStars.append((newStars[i][0], newStars[i][1] + index*(expandFactor - 1)))

# print(newNewStars)

newNewStars.sort(key= lambda a: a[0])

print(newNewStars)

sumDistance = 0

for i in range(len(newNewStars)-1):
    for j in range(i+1, len(newNewStars)):
        pos1 = newNewStars[i]
        pos2 = newNewStars[j]
        sumDistance += abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

print(sumDistance)

618912410702