fText = open("input.txt", "r").read()
arr = [[j for j in i] for i in fText.split("\n")]

for line in arr:
    print("".join(line))
print()

lengthArrR = len(arr)
lengthArrC = len(arr[0])

for i in range(64):
    newArr = [["#" if j == "#" else "." for j in i] for i in arr]
    for rNum in range(lengthArrR):
        for cNum in range(lengthArrC):
            if arr[rNum][cNum] == "O":
                # arr[rNum][cNum] = "."
                for delta in [[1,0], [-1,0], [0,1], [0,-1]]:
                    newR = rNum + delta[0]
                    newC = cNum + delta[1]
                    if newR >= 0 and newR < lengthArrR and newC >= 0 and newC < lengthArrC:
                        if arr[newR][newC] != "#":
                            newArr[newR][newC] = "O"

    arr = newArr
    # for line in arr:
    #     print("".join(line))
    
    # print()

for line in arr:
    print("".join(line))

print()

print(sum([i.count("O") for i in arr]))

#checkerboard pattern for all non rock squares