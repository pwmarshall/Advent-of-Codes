f = open("inputTest.txt", "r")
rocks = f.read().split("\n")
print(rocks)

# colRocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]

# for line in colRocks:
#     print("".join(line))
# print()

# transposed so can move rocks easier, "north" is now "left"

def rollRow(row):
    # print(row)
    returnRow = []
    if row.count("#") == 0:
        rollCount = row.count("O")
        returnRow[:rollCount] = "O"*rollCount
        returnRow[rollCount:] = "." * (len(row)-rollCount)
    else:
        indexRock = row.index("#")
        returnRow = rollRow(row[:indexRock])
        returnRow.append('#') 
        returnRow.extend(rollRow(row[indexRock+1:]))

    # print(returnRow)
    return returnRow

for i in range(4):
    rocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]

    # backRocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]
    print()
    for line in rocks:
        print("".join(line))

    for i in range(len(rocks)):
        rocks[i] = rollRow(rocks[i])

    print()
    for line in rocks:
        print("".join(line))

# for line in colRocks:
#     print("".join(line))

print(sum([sum([len(rocks[i]) - j for j in range(len(rocks[i])) if rocks[i][j] == "O"]) for i in range(len(rocks))]))

## transpose back bc i bad

backRocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]

print()
for line in backRocks:
    print("".join(line))
