f = open("Input.txt", "r")
# print(f.read())
x = f.read().split("\n")
print(x)

actualLowSpots = []

for j in range(len(x)):
    row = x[j]
    rowHighSpots = []
    lastPoint = -1
    increased = 0
    # print(len(row))
    for i in range(len(row)):
        point = row[i]
        if int(point) == 9:
            rowHighSpots.append(i)

    print(rowHighSpots)

    for highSpot in rowHighSpots:
        if j == 0:
            # print("firstRow")
            nextRow = x[j+1]

        elif j == len(x)-1:
            # print("lastRow")
            lastRow = x[j-1]

        else:
            # print("Row")
            nextRow = x[j + 1]
            lastRow = x[j - 1]






