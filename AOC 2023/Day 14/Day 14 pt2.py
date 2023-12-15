f = open("input.txt", "r")
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


memory = {}
cycles = 1000000000
for j in range(cycles): # cycles
    key = "".join(["".join([j for j in i]) for i in rocks])
    # print()
    # print(key)
    # print(sum([sum([len(rocks) - i for j in range(len(rocks[i])) if rocks[i][j] == "O"]) for i in range(len(rocks))]), f"after {j} cycles")

    if key in memory:
        print("repeat", j)
        cycleTime = j - memory[key]
        # print(cycleTime)
        cyclesLeft = cycles-j
        # print(cyclesLeft)
        # print(cyclesLeft % cycleTime)
        keySolve = [i for i in memory if memory[i] == (memory[key] + (cyclesLeft % cycleTime))][0]
        # print(memory[keySolve])

        rocks = [[keySolve[i+(j*len(rocks[0]))] for i in range(len(rocks))] for j in range(len(rocks[0]))]

        break
    else:
        memory[key] = j
        for i in range(4): #4 directions
            rocks = [[rocks[i][j] for i in range(len(rocks))] for j in range(len(rocks[0]))]

            if i == 0 or i == 1:
                for i in range(len(rocks)):
                    rocks[i] = rollRow(rocks[i])
            else:
                for i in range(len(rocks)):
                    rocks[i] = rollRowReversed(rocks[i])


# for line in colRocks:
#     print("".join(line))
# for i in range(len(rocks)):
#     print([len(rocks) - i for j in range(len(rocks[i])) if rocks[i][j] == "O"])
print(sum([sum([len(rocks) - i for j in range(len(rocks[i])) if rocks[i][j] == "O"]) for i in range(len(rocks))]), "answer")


# print()
# for line in rocks:
#     print("".join(line))
