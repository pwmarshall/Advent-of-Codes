f = open("inputTest.txt", "r")
grid = [[j for j in i] for i in f.read().split("\n")]
print(grid)


class lightBeam:
    def __init__(self, pos: list, direction: list, history) -> None:
        self.pos = pos
        self.direction = direction
        self.history = history

    def move(self):
        self.pos = [sum(i for i in j) for j in zip(self.pos, self.direction)]
        
        if min(self.pos) < 0 or max(self.pos) >= len(grid[0]):
            return True #delete beam
        
        if tuple(zip(self.pos, self.direction)) in self.history:
            # print("Repeat")
            # print([i for i in zip(self.pos, self.direction)])
            return True
        else:
            self.history[tuple(zip(self.pos, self.direction))] = 1
        
        tile = grid[self.pos[0]][self.pos[1]]
        # print(tile, f"Tile at {self.pos}")

        if tile == "/":
            self.direction = [-1*i for i in self.direction[::-1]]
            # print(self.direction, "new direction")

        elif tile == "\\":
            self.direction = self.direction[::-1]
            # print(self.direction, "new direction")
        
        elif tile == "|":
            if self.direction[1] != 0:
                self.direction = self.direction[::-1]
                newDirection = [-1 * i for i in self.direction]
                newBeam = lightBeam(self.pos, newDirection, self.history)
                return newBeam
            
        elif tile == "-":
            if self.direction[0] != 0:
                self.direction = self.direction[::-1]
                newDirection = [-1 * i for i in self.direction]
                newBeam = lightBeam(self.pos, newDirection, self.history)
                return newBeam
            
        elif tile == ".":
            pass
            

    
    def __str__(self) -> str:
        return f"beam at {self.pos} moving {self.direction}"
        

class allBeams:
    def __init__(self) -> None:
        self.history = {}
        self.beams = [lightBeam([0,-1], [0,1], self.history)]

    def moveAll(self):
        for beam in self.beams:
            value = beam.move()
            if value == True:
                self.beams.remove(beam)
            elif value == None:
                pass
            else:
                self.beams.append(value)


    def getPosAll(self):
        for beam in self.beams:
            print(beam.pos, "beam pos")

    def getHistory(self):
        return self.history
    
    def done(self):
        if len(self.beams) > 0:
            return False
        return True


b = allBeams()
# for i in range(50):
#     b.moveAll()
#     b.getPosAll()
#     print()

while not b.done():
    b.moveAll()
    # b.getPosAll()
    # print()

possss = [[i[0][0], i[1][0]] for i in b.getHistory()]
newPosss = []
[newPosss.append(i) for i in possss if i not in newPosss]
# print(possss)
# print(newPosss)
# print(len(possss))
print(len(newPosss), "answer")


# energyGrid = [["#" if [i,j] in possss else "." for j in range(len(grid[i]))] for i in range(len(grid))]

# [possss.remove([i,j]) for i in range(len(grid)) for j in range(len(grid[i])) if [i,j] in possss]
# print(possss)
# for line in energyGrid:
#     print("".join(line))
# print([["#" if [i,j] in possss else "." for j in range(len(grid[i]))] for i in range(len(grid))])