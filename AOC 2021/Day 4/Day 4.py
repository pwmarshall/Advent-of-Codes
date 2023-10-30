import math

f = open("Input.txt", "r")
# print(f.read())
x = f.read().split("\n\n")
print(x)

drawn = x[0]
drawnArr = drawn.split(",")
x.pop(0)
print(drawnArr)
boards = []
for board in x:
    # print(board + "\n")
    ree = board.replace("\n ", "\n")
    rows = ree.split("\n")
    # print(rows)
    newRows = []
    for row in rows:
        # print(row)
        nodouble = row.replace("  ", " ")
        rowArr = nodouble.split(" ")
        if rowArr[0] == "":
            rowArr.pop(0)
        newRows.append(rowArr)
    boards.append(newRows)
    # print(newRows)

print(boards)

indexsOfFinalRow = []
indexsOfFinalColumn = []

for board in boards:  # cycle through all boards
    print(board)

    for row in board:
        print(row)
        count = 0

        for number in drawnArr:
            if number in row:
                count += 1
                if count == 5:
                    index = drawnArr.index(number)
                    indexsOfFinalRow.append(index)

    for column in range(5):
        count = 0
        tempColumn = []
        for row in board:
            print(row[column])
            tempColumn.append(row[column])

        for number in drawnArr:
            if number in tempColumn:
                count += 1
                if count == 5:
                    index = drawnArr.index(number)
                    indexsOfFinalColumn.append(index)

print(drawnArr)
print(indexsOfFinalRow)
print(indexsOfFinalColumn)

# part 1
# smallest = 1000
# for indexs in indexsOfFinalRow:
#     if indexs < smallest:
#         smallest = indexs
#
# smallestR = smallest
# print(smallest)
#
# smallest = 1000
# for indexs in indexsOfFinalColumn:
#     if indexs < smallest:
#         smallest = indexs
#
# smallestC = smallest
# print(smallest)
#
# if smallestR < smallestC:
#     solution = indexsOfFinalRow.index(smallestR)
#     lastNumberIndex = smallestR
# else:
#     solution = indexsOfFinalColumn.index(smallestC)
#     lastNumberIndex = smallestC


# part 2
largest = 0
counter = 0
boardSmallest = 1000
boardSmallestRowArr = []

# need to find the smallest out of every group of 5

for indexs in indexsOfFinalRow:

    if indexs < boardSmallest:
        boardSmallest = indexs

    counter += 1

    if counter % 5 == 0 and counter != 0:
        boardSmallestRowArr.append(boardSmallest)
        boardSmallest = 1000

counter = 0
boardSmallest = 1000
boardSmallestColumnArr = []

for indexs in indexsOfFinalColumn:

    if indexs < boardSmallest:
        boardSmallest = indexs

    counter += 1

    if counter % 5 == 0 and counter != 0:
        boardSmallestColumnArr.append(boardSmallest)
        boardSmallest = 1000

print(boardSmallestRowArr)
print(boardSmallestColumnArr)

boardActualSmallestNoMatterWhat = []

for i in range(len(boardSmallestRowArr)):
    if boardSmallestRowArr[i] > boardSmallestColumnArr[i]:
        boardActualSmallestNoMatterWhat.append((boardSmallestColumnArr[i]))
    else:
        boardActualSmallestNoMatterWhat.append((boardSmallestRowArr[i]))

print(boardActualSmallestNoMatterWhat)

for indexs in boardActualSmallestNoMatterWhat:
    if indexs > largest:
        largest = indexs

print(largest)

solution = boardActualSmallestNoMatterWhat.index(largest)
lastNumberIndex = largest

print(solution)

# solBoard = math.floor(solution / 5)
# print(solBoard)

print(boards[solution])
sum = 0
print(drawnArr[:lastNumberIndex + 1])
for rows in boards[solution]:
    for number in rows:
        # print(number)
        if number in drawnArr[:lastNumberIndex + 1]:
            continue
        else:
            sum += int(number)

print(sum)
print(drawnArr[lastNumberIndex])

print(sum * int(drawnArr[lastNumberIndex]))

# for number in row:
#     if number in drawnArr:
#         count += 1
#         # print(count)
#
# if count == 5:
#     print("bingo")

# for row in board:
#     print(row)
#     print(number)
#     if number in row:
#         index = row.index(number)
