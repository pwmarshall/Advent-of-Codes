f = open("input.txt", "r")
#print(f.read())
lines = f.read().split("\n")
print(lines)

ints = ["0","1","2","3","4","5","6","7","8","9"]

def numFind(xf,yf, direction):
    if yf < 0 or yf >= len(lines[0]):
        return ""

    if lines[xf][yf] in ints:
        if direction == 0:
            return numFind(xf, yf - 1, -1) + lines[xf][yf] + numFind(xf, yf + 1, 1)
        elif direction == 1:
            return lines[xf][yf] + numFind(xf, yf + 1, 1)
        elif direction == -1:
            return numFind(xf, yf - 1, -1) + lines[xf][yf]
        

    return ""
    

def search(xf,yf):
    sum = 0

    numsFound = 0
    nums = []

    for deltaX in range(-1,2):
        rowNum = False
        
        newX = xf + deltaX
        for deltaY in range(-1,2):
            newY = yf + deltaY

            if newX >= 0 and newX < len(lines) and newY >= 0 and newY < len(lines[0]) and not (newX == xf and newY == yf):
                # print(f"Checking {newX}, {newY}. Value {lines[newX][newY]}")

                if lines[newX][newY] in ints:
                    if rowNum:
                        continue
                    else:
                        num = int(numFind(newX,newY, 0))
                        nums.append(num)
                        numsFound += 1
                        # print(f"Number {num} found at {newX}, {newY}")
                        rowNum = True

                elif lines[newX][newY] == ".":
                    rowNum = False
                else:
                    print("Overlap?")
            elif newX == xf and newY == yf:
                rowNum = False
                

    if numsFound == 2:
        return nums[0] * nums[1]
    
    return 0


x = 0
y = 0

notSymbols = ["0","1","2","3","4","5","6","7","8","9", "."]

sum = 0
for line in lines:

    y=0
    
    for character in line:
        if character == "*":
            # print(f"Symbol at {x}, {y}")
            sum += search(x,y)

        y += 1

    x += 1

print(sum)


