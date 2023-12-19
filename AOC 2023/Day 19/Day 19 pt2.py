f = open("input.txt", "r")
workflows, ratings = (fsplit:=f.read().split("\n\n"))[0].split("\n"), fsplit[1].split("\n")

print(workflows)
print(ratings)

workflowDict = {(isplit:=i.split("{"))[0] : [j.split(":") for j in isplit[1][:-1].split(",")] for i in workflows}

print(workflowDict)

class Rating():
    def __init__(self, x, m, a, s) -> None:
        self.x, self.m, self.a, self.s = x, m, a, s

    def getLetter(self, letter):
        if letter == "x":
            return self.x
        elif letter == "m":
            return self.m
        elif letter == "a":
            return self.a
        elif letter == "s":
            return self.s
    
    # def sumRating(self):
    #     return sum([self.x, self.m, self.a, self.s])
    
    def numCombinations(self):
        return len(self.x)*len(self.m)*len(self.a)*len(self.s)
        

approvedSum = 0
queue = []
queue.append([Rating(range(1,4001), range(1,4001), range(1,4001), range(1,4001)), "in"])

while len(queue) > 0:
    r, currentWorkflow = queue.pop(0)

    while currentWorkflow != "A" and currentWorkflow != "R":
        for rule in workflowDict[currentWorkflow]:
            if len(rule) == 1:
                currentWorkflow = rule[0]
                break
            else:
                num = int(rule[0][2:])
                letter = rule[0][0]
                letterRange = r.getLetter(letter)
                
                if rule[0][1] == ">":
                    if num in letterRange:
                        if letter == "x":
                            newRange = range(num + 1, r.x.stop)
                            queue.append([Rating(newRange, r.m, r.a, r.s), rule[1]]) 
                            r.x = range(r.x.start, num+1)
                        elif letter == "m":
                            newRange = range(num + 1, r.m.stop)
                            queue.append([Rating(r.x, newRange, r.a, r.s), rule[1]])
                            r.m = range(r.m.start, num+1)
                        elif letter == "a":
                            newRange = range(num + 1, r.a.stop)
                            queue.append([Rating(r.x, r.m, newRange, r.s), rule[1]])
                            r.a = range(r.a.start, num+1)
                        elif letter == "s":
                            newRange = range(num + 1, r.s.stop)
                            queue.append([Rating(r.x, r.m, r.a, newRange), rule[1]])
                            r.s = range(r.s.start, num+1)

                    elif letterRange.start > num:
                        currentWorkflow = rule[1]
                        break

                else:
                    if num in letterRange:
                        if letter == "x":
                            newRange = range(r.x.start, num)
                            queue.append([Rating(newRange, r.m, r.a, r.s), rule[1]])
                            r.x = range(num, r.x.stop)
                        elif letter == "m":
                            newRange = range(r.m.start, num)
                            queue.append([Rating(r.x, newRange, r.a, r.s), rule[1]])
                            r.m = range(num, r.m.stop)
                        elif letter == "a":
                            newRange = range(r.a.start, num)
                            queue.append([Rating(r.x, r.m, newRange, r.s), rule[1]])
                            r.a = range(num, r.a.stop)
                        elif letter == "s":
                            newRange = range(r.s.start, num)
                            queue.append([Rating(r.x, r.m, r.a, newRange), rule[1]])
                            r.s = range(num, r.s.stop)

                    elif letterRange.stop < num:
                        currentWorkflow = rule[1]
                        break

    if currentWorkflow == "A":
        approvedSum += r.numCombinations()

print(approvedSum)