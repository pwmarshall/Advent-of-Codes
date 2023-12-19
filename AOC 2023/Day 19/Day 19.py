f = open("inputTest.txt", "r")
workflows, ratings = (fsplit:=f.read().split("\n\n"))[0].split("\n"), fsplit[1].split("\n")

print(workflows)
print(ratings)

workflowDict = {(isplit:=i.split("{"))[0] : [j.split(":") for j in isplit[1][:-1].split(",")] for i in workflows}

print(workflowDict)

class Rating():
    def __init__(self, s) -> None:
        self.x, self.m, self.a, self.s = [int(i.split("=")[1]) for i in s[1:-1].split(",")]

    def getLetter(self, letter):
        if letter == "x":
            return self.x
        elif letter == "m":
            return self.m
        elif letter == "a":
            return self.a
        elif letter == "s":
            return self.s
    
    def sumRating(self):
        return sum([self.x, self.m, self.a, self.s])
        

approvedSum = 0

for rating in ratings:
    r = Rating(rating)
    currentWorkflow = "in"
    while currentWorkflow != "A" and currentWorkflow != "R":
        for rule in workflowDict[currentWorkflow]:
            if len(rule) == 1:
                currentWorkflow = rule[0]
                break
            else:
                num = int(rule[0][2:])
                if rule[0][1] == ">":
                    if r.getLetter(rule[0][0]) > num:
                        currentWorkflow = rule[1]
                        break

                else:
                    if r.getLetter(rule[0][0]) < num:
                        currentWorkflow = rule[1]
                        break

    if currentWorkflow == "A":
        approvedSum += r.sumRating()

print(approvedSum)