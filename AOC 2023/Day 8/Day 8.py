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


print(lines[0].split(" "))
links = [Node(i.split(" ")[2][1:-1], i.split(" ")[3][:-1], i.split(" ")[0]) for i in lines]
start = None

for link in links:
    searchL = link.getLeft()
    searchR = link.getRight()
    for link2 in links:
        if link2.getName() == searchL:
            link.setLeft(link2)
        if link2.getName() == searchR:
            link.setRight(link2)

    print(link)
    if link.getName() == "AAA":
        start = link

current = start
pointer = start
steps = 0
directionLen = len(direction)

lBool = direction[steps] == "L"

if lBool:
    pointer = current.getLeft()
else:
    pointer = current.getRight()
steps += 1

while pointer.getName() != "ZZZ":
    
    current = pointer

    lBool = direction[steps % directionLen] == "L"
    if lBool:
        pointer = current.getLeft()
    else:
        pointer = current.getRight()
    steps += 1

print(steps)
    


