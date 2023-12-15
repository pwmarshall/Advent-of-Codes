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

def rollRowReversed(row:list):
    # print(row)
    returnRow = []*len(row)
    if row.count("#") == 0:
        rollCount = row.count("O")
        returnRow[:(len(row)-rollCount)] = "." * (len(row)-rollCount)
        returnRow[(len(row)-rollCount):] = "O"*rollCount
    else:
        indexRock = row.index("#")
        returnRow = rollRowReversed(row[:indexRock])
        returnRow.append('#') 
        returnRow.extend(rollRowReversed(row[indexRock+1:]))

    # print(returnRow)
    return returnRow


cycles = 1000000000
percent = cycles / 100
for j in range(cycles): # cycles
    for i in range(4): #4 directions
        rocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]

        # backRocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]
        # print()
        # print(i)
        # for line in rocks:
        #     print("".join(line))

        if i == 0 or i == 1:
            for i in range(len(rocks)):
                rocks[i] = rollRow(rocks[i])
        else:
            for i in range(len(rocks)):
                rocks[i] = rollRowReversed(rocks[i])

        # print()
        # for line in rocks:
        #     print("".join(line))
    
    # print()
    # for line in rocks:
    #     print("".join(line))
    # if (i / cycles) * 100 
    if i % percent == 0:
        print(f"{(i / cycles) * 100}% done")

# for line in colRocks:
#     print("".join(line))

print(sum([sum([len(rocks[i]) - j for j in range(len(rocks[i])) if rocks[i][j] == "O"]) for i in range(len(rocks))]))


print()
for line in rocks:
    print("".join(line))
