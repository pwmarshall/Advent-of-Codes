f = open("inputTest.txt", "r")
grid = [[int(j) for j in i] for i in f.read().split("\n")]
print(grid)

class Node():
    def __init__(self, position, connections = []) -> None:
        self.pos = position
        self.connections = connections
        self.cost = grid[position[0]][position[1]]

    def addConnection(self, node):
        print(f"Connecting {self.pos} to {node.pos}")
        self.connections.append(node)

    def __str__(self) -> str:
        return f"node: pos: {self.pos}, cost: {self.cost}"
    
    def summary(self):
        print(f"Summary of node: pos: {self.pos}, cost: {self.cost}. Connected to ")
        [print(node) for node in self.connections]
        print()


nodeGrid = [[Node([i,j]) for j in range(len(grid[i]))] for i in range(len(grid))]
print(nodeGrid)
[j.summary() for i in nodeGrid for j in i]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        # node = nodeGrid[i][j]
        # node.summary()
        for delta in [[-1,0], [1,0], [0,-1], [0, 1]]:
            newPos = [i + delta[0], j + delta[1]]
            print(newPos, "from", i, j)

            if min(newPos) >= 0 and max(newPos) < len(grid):
                nodeGrid[i][j].addConnection(nodeGrid[newPos[0]][newPos[1]])



startNode = nodeGrid[0][0]
endNode = nodeGrid[len(grid)-1][len(grid[0])-1]
print(startNode.summary())
print(endNode.summary())

class Path():
    def __init__(self, cost = 0, history = []) -> None:
        self.totalCost = cost
        self.history = history
        if history == []:
            self.currentNode = startNode
            self.addNode(startNode)

    def addNode(self, node):
        self.history.append(node)
        self.currentNode = node
        self.totalCost += node.cost



def breadthFirstSearch():
    queue = []

    queue.append(Path())

    while len(queue) > 0:
        p = queue.pop(0)
        print("loop")

        for node in p.currentNode.connections:
            if node not in p.history:
                newP = Path(p.totalCost, p.history)
                newP.addNode(node)
                queue.append(newP)

                if node == endNode:
                    for n in p.history:
                        print(n)
                    # print(p.history)
                    print(p.totalCost, "finished")

        
# breadthFirstSearch()