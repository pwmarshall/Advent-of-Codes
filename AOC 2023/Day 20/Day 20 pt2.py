f = open("input.txt", "r")
modules = f.read().split("\n")

# low pulses: False
# high pulses: True

class mod():
    def __init__(self, name:str, type:str, outs:tuple) -> None:
        self.name = name
        self.type = type #either % or &
        if type == "&":
            self.inputs = {}
        else:
            self.state = False
        self.outs = outs

    def receivePulse(self, info:tuple):
        #return None is no new pulse, otherwise new pulse is return value
        inputName, myName, pulse = info
        if self.type == "%":
            if pulse != True:
                self.state = not self.state
                return self.state
            else:
                return None
            
        else:
            # print(self.inputs)
            self.inputs[inputName] = pulse
            # print(self.inputs)
            if all(self.inputs.values()):
                return False
            else:
                return True
            
    def getStatus(self):
        if self.name == "broadcaster":
            return "B"
        elif self.type == "%":
            return "1" if self.state else "0"
        else:
            return "".join(["1" if i else "0" for i in self.inputs.values()])


def memoryString(mDict):
    return "".join([m.getStatus() for m in mDict.values()])

modDict = {}

for moduleString in modules:
    moduleStringSplit = moduleString.split(" -> ")
    if moduleStringSplit[0] == "broadcaster":
        m = mod("broadcaster", ".", moduleStringSplit[1].split(", "))
    else:
        m = mod(moduleStringSplit[0][1:], moduleStringSplit[0][0], moduleStringSplit[1].split(", "))

    modDict[m.name] = m



for mName in modDict:
    m = modDict[mName]
    if m.type == "&":
        for mName2 in modDict:
            if m.name in modDict[mName2].outs:
                m.inputs[modDict[mName2].name] = False

print(memoryString(modDict))

memory = {}

outSums = [0,0]
count = 1
while True:
    rxCount = 0

    queue = []
    [queue.append(("broadcaster", i, False)) for i in modDict["broadcaster"].outs]

    # pulse format: (from mod name, to mod name, pulse)
    pulseCountLow = 1 # start at one for button press
    pulseCountHigh = 0

    while len(queue) > 0:
        pulse = queue.pop(0)
        # print(pulse)
        if pulse[2]:
            pulseCountHigh += 1
        else:
            pulseCountLow += 1

        if pulse[1] == "rx":
            if not pulse[2]:
                rxCount += 1
            newPulse = None
        else:
            newPulse = modDict[pulse[1]].receivePulse(pulse)

        if newPulse != None:
            [queue.append((pulse[1], i, newPulse)) for i in modDict[pulse[1]].outs]
    

    # mS = memoryString(modDict)
    # print(mS)
    # print(count)

    # if mS in memory or count == 1000:
    #     break
    # memory[mS] = (pulseCountLow, pulseCountHigh)
    if rxCount == 1:
        print(count)
        break
    count += 1
    # outSums[0] += pulseCountLow
    # outSums[1] += pulseCountHigh


# listMemory = [i for i in memory.values()]
# length = len(listMemory)
pulseSumLow = 0
pulseSumHigh = 0

# for i in range(1000):
#     pulseSumLow += listMemory[i % length][0]
#     pulseSumHigh += listMemory[i % length][1]


# print(pulseSumLow * pulseSumHigh)

print(outSums[0] * outSums[1])
