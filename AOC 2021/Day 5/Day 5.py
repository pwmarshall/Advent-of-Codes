f = open("Input.txt", "r")
#print(f.read())
x = f.read().split("\n")
print(x)

lines = []

for line in x:
    points = line.split(" -> ")
    XandYs = []
    for point in points:
        XandY = point.split(",")
        XandYs.append(XandY)
    lines.append(XandYs)

print(lines)

goodLines = []

for line in lines:
    # print(line)
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        goodLines.append(line)

print(goodLines)

pointsOnLines = []

for line in lines:
    if line[0][0] == line[1][0] and int(line[0][1]) < int(line[1][1]):
        for i in range(int(line[0][1]), int(line[1][1])+1):
            pointsOnLines.append([line[0][0], str(i)])
    elif line[0][1] == line[1][1] and int(line[0][0]) < int(line[1][0]):
        for i in range(int(line[0][0]), int(line[1][0])+1):
            pointsOnLines.append([str(i), line[0][1]])
    elif line[0][1] == line[1][1] and int(line[0][0]) > int(line[1][0]):
        for i in range(int(line[1][0]), int(line[0][0])+1):
            pointsOnLines.append([str(i), line[0][1]])
    elif line[0][0] == line[1][0] and int(line[0][1]) > int(line[1][1]):
        for i in range(int(line[1][1]), int(line[0][1])+1):
            pointsOnLines.append([line[0][0], str(i)])
#part 2:
    elif int(line[0][1]) < int(line[1][1]) and int(line[0][0]) < int(line[1][0]):
        for i in range(int(line[0][1]), int(line[1][1])+1):
            add = i - int(line[0][1])
            pointsOnLines.append([str(int(line[0][0])+add), str(i)])
    elif int(line[0][1]) < int(line[1][1]) and int(line[0][0]) > int(line[1][0]):
        for i in range(int(line[0][1]), int(line[1][1])+1):
            add = i - int(line[0][1])
            pointsOnLines.append([str(int(line[0][0])-add), str(i)])
    elif int(line[0][1]) > int(line[1][1]) and int(line[0][0]) < int(line[1][0]):
        for i in range(int(line[1][1]), int(line[0][1])+1):
            add = i - int(line[1][1])
            pointsOnLines.append([str(int(line[1][0])-add), str(i)])
    elif int(line[0][1]) > int(line[1][1]) and int(line[0][0]) > int(line[1][0]):
        for i in range(int(line[1][1]), int(line[0][1])+1):
            add = i - int(line[1][1])
            pointsOnLines.append([str(int(line[1][0])+add), str(i)])

print(pointsOnLines)

count = 0

pointsOnLines2 = []
alreadyCounted = []

for point in pointsOnLines:
    # print(point)
    if point in pointsOnLines2:
        if point in alreadyCounted:
            continue
        else:
            count += 1
            alreadyCounted.append(point)

        # print(point)
        # print(pointsOnLines.index(point))
    else:
        pointsOnLines2.append(point)

print(count)
