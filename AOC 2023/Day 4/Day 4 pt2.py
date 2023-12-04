f = open("input.txt", "r")
#print(f.read())
lines = f.read().split("\n")
print(lines)

cardsCreated = [1] * len(lines)

for line in lines:
    lineSplit = line.split(": ")
    cardNum = int(lineSplit[0].split(" ")[1])
    nums = lineSplit[1]
    numsSplit = nums.split(" | ")
    winningNums = numsSplit[0].split(" ")
    guessNums = numsSplit[1].split(" ")

    matching = 0

    for number in winningNums:
        if number in guessNums:
            matching += 1

    print(f"Card {cardNum} has {matching}")
    for i in range(cardNum, cardNum + matching):
        cardsCreated[i] += cardsCreated[cardNum-1]

    print(cardsCreated)

print(sum(cardsCreated))
