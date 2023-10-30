f = open("Input.txt", "r")
# print(f.read())
x = f.read().split("\n")
print(x)

newX = []
for line in x:
    tempLine = line.split(" | ")
    tempLineArr = []
    for half in tempLine:
        tempLineArr.append(half.split(" "))
    newX.append(tempLineArr)

print(newX)

count = 0

# picture
#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666

segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] #used 1,7,6 aka 2,3,6 can use 4,5,7.  7 dont do much
allWires = ['a','b','c','d','e','f','g']

numbers = []

for line in newX:
    print(line)
    segmentsMatch = [] # put the letter(s) that does that one
    idkWhatToNameThisBackup = 0
    for i in range(7):
        segmentsMatch.append(0)
    # print(segmentsMatch)
    for i in range(4):
        for input in line[0]:
            if len(input) == segments[1] and segmentsMatch[2] == 0: #1
                segmentsMatch[2] = input[0] + "/" + input[1]
            elif len(input) == segments[7] and segmentsMatch[2] != 0 and segmentsMatch[0] == 0 and ("/" in segmentsMatch[2] or idkWhatToNameThisBackup != 0): #7
                if idkWhatToNameThisBackup == 0:
                    for wire in input:
                        if wire in segmentsMatch[2]:
                            continue
                        else:
                            segmentsMatch[0] = wire
                else:
                    for wire in input:
                        if wire in idkWhatToNameThisBackup:
                            continue
                        else:
                            segmentsMatch[0] = wire
            elif len(input) == segments[6] and segmentsMatch[2] != 0 and ("/" in segmentsMatch[2] or idkWhatToNameThisBackup != 0): #0,6,9
                if idkWhatToNameThisBackup == 0:
                    if segmentsMatch[2][0] in input and segmentsMatch[2][2] in input:
                        # print(0 or 9)
                        if segmentsMatch[3] != 0 and "/" in segmentsMatch[3]:
                            if segmentsMatch[3][0] in input and segmentsMatch[3][2] in input:
                                # print(9)
                                #the one not in is the bot left
                                for letter in allWires:
                                    if letter not in input:
                                        segmentsMatch[4] = letter
                            else:
                                #print(0)
                                # the one not in is the mid
                                for letter in allWires:
                                    if letter not in input:
                                        tempLetterArr = segmentsMatch[3].split("/")
                                        tempLetterArr.remove(letter)
                                        segmentsMatch[1] = tempLetterArr[0]
                                        segmentsMatch[3] = letter
                        elif segmentsMatch[3] != 0 and segmentsMatch[1] != 0:
                            if segmentsMatch[3] in input and segmentsMatch[1] in input:
                                # print(9)
                                # the one not in is the bot left
                                for letter in allWires:
                                    if letter not in input:
                                        segmentsMatch[4] = letter
                    else:
                        # print(6)
                        if segmentsMatch[2][0] in input:
                            segmentsMatch[5] = segmentsMatch[2][0]
                            idkWhatToNameThisBackup = segmentsMatch[2]
                            segmentsMatch[2] = segmentsMatch[2][2]

                        else:
                            segmentsMatch[5] = segmentsMatch[2][2]
                            idkWhatToNameThisBackup = segmentsMatch[2]
                            segmentsMatch[2] = segmentsMatch[2][0]
                else:
                    if idkWhatToNameThisBackup[0] in input and idkWhatToNameThisBackup[2] in input:
                        # print(0 or 9)
                        if segmentsMatch[3] != 0 and "/" in segmentsMatch[3]:
                            if segmentsMatch[3][0] in input and segmentsMatch[3][2] in input:
                                # print(9)
                                # the one not in is the bot left
                                for letter in allWires:
                                    if letter not in input:
                                        segmentsMatch[4] = letter
                            else:
                                # print(0)
                                # the one not in is the mid
                                for letter in allWires:
                                    if letter not in input:
                                        tempLetterArr = segmentsMatch[3].split("/")
                                        tempLetterArr.remove(letter)
                                        segmentsMatch[1] = tempLetterArr[0]
                                        segmentsMatch[3] = letter
                        elif segmentsMatch[3] != 0 and segmentsMatch[1] != 0:
                            if segmentsMatch[3] in input and segmentsMatch[1] in input:
                                # print(9)
                                # the one not in is the bot left
                                for letter in allWires:
                                    if letter not in input:
                                        segmentsMatch[4] = letter

            elif len(input) == segments[4] and segmentsMatch[2] != 0 and segmentsMatch[3] == 0:
                leftOut = []
                if len(segmentsMatch[2]) == 1:
                    for letter in input:
                        if letter in segmentsMatch[2] or letter in segmentsMatch[5]:
                            continue
                        else:
                            leftOut.append(letter)
                else:
                    for letter in input:
                        if letter in segmentsMatch[2]:
                            continue
                        else:
                            leftOut.append(letter)
                segmentsMatch[3] = leftOut[0] + "/" + leftOut[1]

            elif len(input) == segments[8] and segmentsMatch[1] != 0:
                for letter in input:
                    if letter in segmentsMatch:
                        continue
                    else:
                        segmentsMatch[6] = letter


    print(segmentsMatch)

    # print(line)
    number = ""

    segmentsMatchLetters = []
    for i in range(10):
        if i == 1 or i == 4 or i == 7 or i == 8:
            segmentsMatchLetters.append(0)
        elif i == 0:
            segmentsMatchLetters.append(segmentsMatch[0]+segmentsMatch[1]+segmentsMatch[2]+segmentsMatch[4]+segmentsMatch[5]+segmentsMatch[6])
        elif i == 2:
            segmentsMatchLetters.append(segmentsMatch[0]+segmentsMatch[2]+segmentsMatch[3]+segmentsMatch[4]+segmentsMatch[6])
        elif i == 3:
            segmentsMatchLetters.append(segmentsMatch[0]+segmentsMatch[2]+segmentsMatch[3]+segmentsMatch[5]+segmentsMatch[6])
        elif i == 5:
            segmentsMatchLetters.append(segmentsMatch[0]+segmentsMatch[1]+segmentsMatch[3]+segmentsMatch[5]+segmentsMatch[6])
        elif i == 6:
            segmentsMatchLetters.append(segmentsMatch[0]+segmentsMatch[1]+segmentsMatch[3]+segmentsMatch[4]+segmentsMatch[5]+segmentsMatch[6])
        elif i == 9:
            segmentsMatchLetters.append(segmentsMatch[0]+segmentsMatch[1]+segmentsMatch[2]+segmentsMatch[3]+segmentsMatch[5]+segmentsMatch[6])

    for output in line[1]:
        if len(output) == segments[1]:
            number = number + "1"
        elif len(output) == segments[4]:
            number = number + "4"
        elif len(output) == segments[7]:
            number = number + "7"
        elif len(output) == segments[8]:
            number = number + "8"
        elif sorted(output) == sorted(segmentsMatchLetters[0]):
            number = number + "0"
        elif sorted(output) == sorted(segmentsMatchLetters[2]):
            number = number + "2"
        elif sorted(output) == sorted(segmentsMatchLetters[3]):
            number = number + "3"
        elif sorted(output) == sorted(segmentsMatchLetters[5]):
            number = number + "5"
        elif sorted(output) == sorted(segmentsMatchLetters[6]):
            number = number + "6"
        elif sorted(output) == sorted(segmentsMatchLetters[9]):
            number = number + "9"
    print(number)
    numbers.append(number)

print(numbers)
sum = 0

for number in numbers:
    sum += int(number)

print(sum)
