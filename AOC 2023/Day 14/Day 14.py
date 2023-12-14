f = open("input.txt", "r")
rocks = f.read().split("\n")
print(rocks)

colRocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]

for line in colRocks:
    print("".join(line))
print()

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

for i in range(len(colRocks)):
    colRocks[i] = rollRow(colRocks[i])

# for line in colRocks:
#     print("".join(line))

print(sum([sum([len(colRocks[i]) - j for j in range(len(colRocks[i])) if colRocks[i][j] == "O"]) for i in range(len(colRocks))]))

## transpose back bc i bad

# backRocks = [[colRocks[i][j] for i in range(len(colRocks))] for j in range(len(colRocks[0]))]

# print()
# for line in backRocks:
#     print("".join(line))
