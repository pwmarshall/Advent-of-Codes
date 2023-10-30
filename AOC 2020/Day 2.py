
f = open("Day 2 Input.txt", "r")
#print(f.read())
x = f.read().split("\n")
x.pop()
#print(x)

count = 0

for i in range(len(x)):
    x[i] = x[i].split(":")
    letter = x[i][0][-1]
    #print(letter)

    #part 1

#    actualTimes = x[i][1].count(letter)
#    #print(actualTimes)
#    neededTimes = x[i][0][:-1].split("-")
#    #print(neededTimes)
#    if actualTimes >= int(neededTimes[0]) and actualTimes <= int(neededTimes[1]):
#        count += 1
#        print("passed")

    #part 2

    neededPositions = x[i][0][:-1].split("-")
    #print(x[i][1][int(neededPositions[0])])

    if x[i][1][int(neededPositions[0])] == letter and x[i][1][int(neededPositions[1])] != letter:
        #print("hey i think this works")
        count += 1
    elif x[i][1][int(neededPositions[1])] == letter and x[i][1][int(neededPositions[0])] != letter:
        count += 1


print(count)


f.close()
