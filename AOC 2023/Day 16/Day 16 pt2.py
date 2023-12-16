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

    def moveReverse(self):
        self.pos = [sum(i for i in j) for j in zip(self.pos, [-1 * i for i in self.direction])]

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
    def __init__(self, pt1 = True, history = {}) -> None:
        self.history = history
        if pt1:
            self.beams = [lightBeam([0,-1], [0,1], self.history)]
        else:
            self.beams = []

    def moveAll(self):
        for beam in self.beams:
            value = beam.move()
            if value == True:
                self.beams.remove(beam)
            elif value == None:
                pass
            else:
                self.beams.append(value)

    def moveAllReverse(self):
        for beam in self.beams:
            value = beam.moveReverse()
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
    
    def addBeam(self, pos:list, direction: list):
        self.beams.append(lightBeam(pos, direction, self.history))
    



b = allBeams()
# for i in range(50):
#     b.moveAll()
#     b.getPosAll()
#     print()

while not b.done():
    b.moveAll()
    # b.getPosAll()
    # print()

hist = b.getHistory()
print(hist)
possss = [[i[0][0], i[1][0]] for i in hist]
newPosss = []
[newPosss.append(i) for i in possss if i not in newPosss]
print(len(newPosss), "answer")


print([i for i in hist if i[0][0] == 7 and i[1][0] == 3])

length = len(grid)
for i in range(length):
    for j in range(length):
        tile = grid[i][j]
        if tile == "-":
            if tuple(zip([i, j], [1,0])) not in hist and (tuple(zip([i, j], [0,1])) in hist or tuple(zip([i, j], [0,-1])) in hist):
                reverseBeams1 = allBeams(False, hist)

                reverseBeams1.addBeam([i,j], [1, 0])
                print("adding beam pos:", [i, j])

                while not reverseBeams1.done():
                    reverseBeams1.moveAllReverse()
                
                added1 = [[i[0][0], i[1][0]] for i in reverseBeams1.getHistory() if [i[0][0], i[1][0]] not in newPosss]
                print(len(added1), "1")
            elif tuple(zip([i, j], [-1,0])) not in hist and (tuple(zip([i, j], [0,1])) in hist or tuple(zip([i, j], [0,-1])) in hist):
                reverseBeams2 = allBeams(False, hist)

                reverseBeams2.addBeam([i,j], [-1, 0])
                print("adding beam pos:", [i, j])

                while not reverseBeams2.done():
                    reverseBeams2.moveAllReverse()
                
                added2 = [[i[0][0], i[1][0]] for i in reverseBeams2.getHistory() if [i[0][0], i[1][0]] not in newPosss]
                print(len(added2), "2")
        elif tile == "|":
            if tuple(zip([i, j], [0,1])) not in hist and (tuple(zip([i, j], [1,0])) in hist or tuple(zip([i, j], [-1,0])) in hist):
                reverseBeams3 = allBeams(False, hist)

                reverseBeams3.addBeam([i,j], [0, 1])
                print("adding beam pos:", [i, j])

                while not reverseBeams3.done():
                    reverseBeams3.moveAllReverse()
                    reverseBeams3.getPosAll()
                
                added3 = [[i[0][0], i[1][0]] for i in reverseBeams3.getHistory() if [i[0][0], i[1][0]] not in newPosss]
                print(len(added3), "3")
            elif tuple(zip([i, j], [0,1])) not in hist and (tuple(zip([i, j], [1,0])) in hist or tuple(zip([i, j], [-1,0])) in hist):
                reverseBeams4 = allBeams(False, hist)

                reverseBeams4.addBeam([i,j], [0, -1])
                print("adding beam pos:", [i, j])

                while not reverseBeams4.done():
                    reverseBeams4.moveAllReverse()
                
                added4 = [[i[0][0], i[1][0]] for i in reverseBeams4.getHistory() if [i[0][0], i[1][0]] not in newPosss]
                print(len(added4), "4")

# reverseBeams.getPosAll()

# while not reverseBeams.done():
#     reverseBeams.moveAllReverse()
#     # reverseBeams.getPosAll()
#     # print()

# newHist = reverseBeams.getHistory()
# # print(newHist)
# possss2 = [[i[0][0], i[1][0]] for i in newHist]
# newPosss2 = []
# [newPosss2.append(i) for i in possss2 if i not in newPosss2]
# # print(newPosss2)
# print(len(newPosss2), "answer")


# testingPos = []
# [testingPos.append(i) for i in possss2 if i not in newPosss]
# print(testingPos)
