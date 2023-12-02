f = open("input1.txt", "r")
#print(f.read())
x = f.read().split("\n")
print(x)


## part 1

redMax = 12
greenMax = 13
blueMax = 14

sum = 0

for line in x:
    # print(line)

    game = line.split(":")
    ID = int(game[0].split(" ")[1])

    pulls = game[1].split(";")

    impossible = False

    for pull in pulls:
        # print(pull)
        counts = pull.split(",")
        if impossible:
            break

        for count in counts:
            if impossible:
                break
            # print(count)
            countSplit = count.split(" ")
            num = int(countSplit[1])
            color = countSplit[2]

            if color == "red":
                if num > redMax:
                    impossible = True
            elif color == "green":
                if num > greenMax:
                    impossible = True
            elif color == "blue":
                if num > blueMax:
                    impossible = True
            else:
                print("WTF")
            
    if not impossible:
        sum += ID
        # print(ID)

print(sum)




## part 2

sum = 0

for line in x:
    # print(line)

    game = line.split(":")
    ID = int(game[0].split(" ")[1])

    pulls = game[1].split(";")

    redMin = 0
    blueMin = 0
    greenMin = 0

    for pull in pulls:
        # print(pull)
        counts = pull.split(",")

        for count in counts:
            # print(count)
            countSplit = count.split(" ")
            num = int(countSplit[1])
            color = countSplit[2]

            if color == "red":
                if num > redMin:
                    redMin = num
            elif color == "green":
                if num > greenMin:
                    greenMin = num
            elif color == "blue":
                if num > blueMin:
                    blueMin = num
            else:
                print("WTF")
            
    power = redMin * greenMin * blueMin
    sum += power

print(sum)