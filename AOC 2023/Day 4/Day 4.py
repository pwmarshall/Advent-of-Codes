f = open("input.txt", "r")
#print(f.read())
lines = f.read().split("\n")
print(lines)

sum = 0

for line in lines:
    lineSplit = line.split(": ")
    nums = lineSplit[1]
    numsSplit = nums.split(" | ")
    winningNums = numsSplit[0].split(" ")
    guessNums = numsSplit[1].split(" ")

    cardTotal = 0

    for number in winningNums:
        if number in guessNums:
            if cardTotal == 0:
                cardTotal = 1
            else:
                cardTotal *= 2


    print(f"{lineSplit[0]} has a score of {cardTotal}")
    sum += cardTotal

print(sum)