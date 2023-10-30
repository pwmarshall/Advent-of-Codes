f = open("Input.txt", "r")
# print(f.read())
x = f.read().split("\n")
print(x)

actualLowSpots = []

for j in range(len(x)):
    row = x[j]
    rowLowSpots = []
    lastPoint = -1
    increased = 0
    # print(len(row))
    for i in range(len(row)):
        # print(i)
        point = row[i]
        if i == 0:
            # print("first")
            lastPoint = point
        elif i == len(row) - 1:
            # print("last")
            if point < lastPoint:
                rowLowSpots.append(i)
        else:
            # print(lastPoint + " " + point + " " + str(increased))
            # print("else")
            if point < lastPoint:
                increased = 0
                # last point not a low spot
            elif increased == 0:
                rowLowSpots.append(i - 1)
                increased = 1
            else:
                increased = 1
            lastPoint = point
    print(rowLowSpots)
    for lowSpot in rowLowSpots:
        # if row[lowSpot] == 0:
        #     actualLowSpots.append(row[lowSpot])
        if j == 0:
            # print("firstRow")
            nextRow = x[j+1]
            if int(row[lowSpot]) < int(nextRow[lowSpot]):
                actualLowSpots.append(int(row[lowSpot]))
        elif j == len(x)-1:
            # print("lastRow")
            lastRow = x[j-1]
            if int(row[lowSpot]) < int(lastRow[lowSpot]):
                actualLowSpots.append(int(row[lowSpot]))
        else:
            # print("Row")
            nextRow = x[j + 1]
            lastRow = x[j - 1]
            if int(row[lowSpot]) < int(nextRow[lowSpot]) and int(row[lowSpot]) < int(lastRow[lowSpot]):
                actualLowSpots.append(int(row[lowSpot]))

print(actualLowSpots)

riskSum = 0
for height in actualLowSpots:
    risk = height + 1
    riskSum += risk

print(riskSum)


