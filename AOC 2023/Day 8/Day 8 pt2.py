f = open("input.txt", "r")
#print(f.read())
text = f.read().split("\n\n")
# print(text)

direction = text[0]
lines = text[1].split("\n")

print(direction)
print(lines)


class Node:

    def __init__(self, left, right, name) -> None:
        self.left = left
        self.right = right
        self.name = name

    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} = ({self.left.getName()}, {self.right.getName()})"


# print(lines[0].split(" "))
links = [Node(i.split(" ")[2][1:-1], i.split(" ")[3][:-1], i.split(" ")[0]) for i in lines]
starts = [] # currents in first try

for link in links:
    searchL = link.getLeft()
    searchR = link.getRight()
    for link2 in links:
        if link2.getName() == searchL:
            link.setLeft(link2)
        if link2.getName() == searchR:
            link.setRight(link2)

    # print(link)
    if link.getName()[2] == "A":
        starts.append([link, link])


print([str(i[0]) for i in starts])
directionLen = len(direction)
steps = 0

for start in starts:
    current = start[0]
    pointer = start[0]
    steps = 0
    directionLen = len(direction)

    lBool = direction[steps] == "L"

    if lBool:
        pointer = current.getLeft()
    else:
        pointer = current.getRight()
    steps += 1

    while pointer.getName()[2] != "Z":
        
        current = pointer

        lBool = direction[steps % directionLen] == "L"
        if lBool:
            pointer = current.getLeft()
        else:
            pointer = current.getRight()
        steps += 1

    print(steps) #find lcm of all them, (assuming repeats equally which it does)

# take one fail

# #first step
# for i in range(len(currents)):

#     current = currents[i][0]

#     lBool = direction[steps] == "L"
#     if lBool:
#         currents[i][1] = current.getLeft()
#     else:
#         currents[i][1] = current.getRight()

# steps += 1

# # print([i[1].getName() for i in currents])

# def finish(arr):

#     for item in arr:
#         if item[1].getName()[2] != "Z":
#             return False
        
#     return True

# while not finish(currents):

#     for i in range(len(currents)):

#         currents[i][0] = currents[i][1]

#         current = currents[i][0]

#         lBool = direction[steps % directionLen] == "L"
#         if lBool:
#             currents[i][1] = current.getLeft()
#         else:
#             currents[i][1] = current.getRight()

#     # print(f"After step #{steps} all links: {[i[1].getName() for i in currents]}")
#     steps += 1
 
print(steps)
    


