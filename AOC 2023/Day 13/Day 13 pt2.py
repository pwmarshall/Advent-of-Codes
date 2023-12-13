f = open("input.txt", "r")
patterns = [i.split("\n") for i in f.read().split("\n\n")]
print(patterns)

# know for test: 
# no first column on 1
# no first row on 2

answerSum = 0

# test vertical
for pattern in patterns:
    # print()

    for i in range(1, len(pattern[0])*2 - 3):
        # print(i)
        if i % 2 == 1:
            # print(str(i//2 + 1) + " on")
            testPattern = [pattern[j][i//2 + 1:] for j in range(len(pattern))]
        else:
            # print("up to " + str(i//2))
            testPattern = [pattern[j][: - i//2] for j in range(len(pattern))]
        
        # for line in testPattern:
        #     print(line)

        lengthRow = len(testPattern[0])
        errors = 0
        if lengthRow % 2 == 0:
            for row in testPattern:
                for index in range(lengthRow//2):
                    if row[index] != row[(lengthRow - 1) - index]:
                        errors += 1
                        
            # print(errors)

            if errors == 1:
                if i % 2 == 1:
                    print(f"Columns to left: {lengthRow//2 + (i//2 + 1)}")
                    answerSum += lengthRow//2 + (i//2 + 1)
                else:
                    print(f"Columns to left: {lengthRow//2}")
                    answerSum += lengthRow//2
        else:
            # print("Not even")
            pass

        if errors == 1:
            break
        # print()
        

# test horizontal
for pattern in patterns:
    # print()

    for i in range(1, len(pattern)*2 - 3):
        # print(i)
        if i % 2 == 1:
            # print(str(i//2 + 1) + " on")
            testPattern = pattern[i//2 + 1:]
        else:
            # print("up to " + str(i//2))
            testPattern = pattern[: - i//2]
        
        # for line in testPattern:
        #     print(line)

        numRows = len(testPattern)
        errors = 0

        if numRows % 2 == 0:
            for colIndex in range(len(testPattern[0])):
                for index in range(numRows//2):
                    if testPattern[index][colIndex] != testPattern[(numRows - 1) - index][colIndex]:
                        errors += 1

            # print(errors)

            if errors == 1:
                if i % 2 == 1:
                    print(f"Rows Above: {numRows//2 + (i//2 + 1)}")
                    answerSum += (numRows//2 + (i//2 + 1)) * 100
                else:
                    print(f"Rows Above: {numRows//2}")
                    answerSum += (numRows//2) * 100
        else:
            # print("Not even")
            pass

        if errors == 1:
            break
        # print()
        

print(answerSum)