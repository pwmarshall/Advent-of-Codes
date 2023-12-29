fText = open("inputTest.txt", "r").read()
arr = [[j for j in i] for i in fText.split("\n")]

lengthArrX = len(arr)
lengthArrY = len(arr[0])

def depthSearch(pos):
    tile = arr[pos[0]][pos[1]]
    # arr[pos[0]][pos[1]] = "O"

    if tile == ".":
        
        breathSearch(pos)
    
    else:
        delta = []
        if tile == ">":
            delta = [0, 1]
        elif tile == "v":
            delta = [1, 0]
        elif tile == "<":
            delta = [0, -1]
        elif tile == "^":
            delta == [-1, 0]
        else:
            print(pos)
            print(tile)
            print("WHY")

        newX = pos[0] + delta[0]
        newY = pos[1] + delta[1]

        if newX >= 0 and newX < lengthArrX and newY >= 0 and newY < lengthArrY:
            return depthSearch([newX, newY]) + 1
        return 0
    
def breathSearch(posStart):
    queue = []
    history = []
    queue.append(posStart)

    while len(queue) > 0:
        pos = queue.pop(0)
        history.append(pos)
        tile = arr[pos[0]][pos[1]]
        # arr[pos[0]][pos[1]] = "O"

        if tile == ".":
            arr[pos[0]][pos[1]] = "O"
            returns = [0]
            for delta in [[1,0], [-1,0], [0,1], [0,-1]]:
                newX = pos[0] + delta[0]
                newY = pos[1] + delta[1]

                if newX >= 0 and newX < lengthArrX and newY >= 0 and newY < lengthArrY:
                    if (newTile := arr[newX][newY]) == ".":
                        queue.append([newX, newY])
                    elif newTile == ">" or newTile == "<" or newTile == "v" or newTile == "^":
                        return depthSearch([newX, newY]) + len(history)
            
    return 0

print(depthSearch([0,1]))