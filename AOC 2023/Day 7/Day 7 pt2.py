f = open("input.txt", "r")
#print(f.read())
lines = f.read().split("\n")
print(lines)

def handType(hand: str):
    # 1 -> high card
    # 2 -> one pair
    # ...
    # 7 -> 5 of kind

    count = {}
    for card in hand:
        try:
            num = count[card]
        except:
            num = 0
        count[card] = num + 1

    # print(count)
    # print(max(count, key=lambda a: count[a]))

    try:
        num = count["J"]
        if num != 5:
            count[max(count, key=lambda a: count[a])] += num
            del count["J"]
        else:
            pass
    except:
        pass

    length = len(count)
    if length == 5:
        # print("High Card")
        return 1
    elif length == 4:
        # print("One Pair")
        return 2
    elif length == 3:
        #two pair or three of kind
        if (count[max(count, key=lambda a: count[a])] == 2):
            # print("Two Pair")
            return 3
        else:
            # print("Three of a Kind")
            return 4
    elif length == 2:
        #full house or 4 of kind
        if (count[max(count, key=lambda a: count[a])] == 3):
            # print("Full House")
            return 5
        else:
            # print("Four of a Kind")
            return 6
    elif length == 1:
        # print("Five of a Kind")
        return 7
    
    else:
        print("WTF")
        print(count)
        print(hand)

        
    
arr = [[i.split(" ")[0], int(i.split(" ")[1]), handType(i.split(" ")[0])] for i in lines]

cardValue = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0
}


print(arr)

for i in range(len(arr)):
    change = False
    for j in range(len(arr)-1):
        swap = False
        typej1 = arr[j][2]
        typej2 = arr[j+1][2]
        if typej1 > typej2:
            swap = True
        elif typej1 == typej2:
            z = 0
            while True:
                letter1 = arr[j][0][z]
                letter2 = arr[j+1][0][z]
                if cardValue[letter1] > cardValue[letter2]:
                    swap = True
                    break
                elif cardValue[letter1] == cardValue[letter2]:
                    z += 1
                else:
                    break

        if swap:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            change = True


    if not change:
        break

print(arr)

sum = 0
for i in range(len(arr)):
    sum += (i+1) * arr[i][1]

print(sum)