f = open("input.txt", "r")
#print(f.read())
cats = f.read().split("\n\n")
print(cats)


class AOCmap:

    def __init__(self) -> None:
        self.ranges = []

    def addRange(self, destStart, sourceStart, length):
        self.ranges.append([range(sourceStart, sourceStart+length, 1), destStart - sourceStart])
        # if in self.ranges[][0] transform by self.ranges[][1]

    def add(self, tuple):
        self.addRange(int(tuple[0]), int(tuple[1]), int(tuple[2]))

    def transform(self, seeds):
        newSeeds = []
        

        for seedRange in seeds:
            transfered = []
            for arr in self.ranges:
                print(f"Transform {seedRange} on {arr[0]} by {arr[1]}")
                start = arr[0].start
                stop = arr[0].stop
                delta = arr[1]
                if start in seedRange:
                    if stop in seedRange:
                        newSeeds.append(range(start + delta, stop + delta))
                        transfered.append(range(start, stop))
                    else:
                        newSeeds.append(range(start + delta, seedRange.stop + delta))
                        transfered.append(range(start, seedRange.stop))
                elif start < seedRange.start and stop > seedRange.start:
                    if stop in seedRange:
                        newSeeds.append(range(seedRange.start + delta, stop + delta))
                        transfered.append(range(seedRange.start, stop))
                    else:
                        newSeeds.append(range(seedRange.start + delta, seedRange.stop + delta))
                        transfered.append(range(seedRange.start, seedRange.stop))
                
            # print(transfered)
            transfered.sort(key = lambda a: a.start)
            # print(transfered)
            lastStop = -1
            if len(transfered) > 0:
                for transferedRange in transfered:
                    if transferedRange.start == seedRange.start:
                        lastStop = transferedRange.stop
                    elif transferedRange.start == lastStop:
                        lastStop = transferedRange.stop
                    elif lastStop == -1:
                        newSeeds.append(range(seedRange.start, transferedRange.start))
                        lastStop = transferedRange.stop
                    else:
                        newSeeds.append(range(lastStop, transferedRange.start))
                        lastStop = transferedRange.stop
            else:
                newSeeds.append(range(seedRange.start, seedRange.stop))

            if lastStop != seedRange.stop and lastStop != -1:
                newSeeds.append(range(lastStop, seedRange.stop))
            
        return newSeeds




maps = []
seeds = []
mapIndex = 0

for cat in cats:
    
    print(cat)
    lines = cat.split("\n")

    line0Split = lines[0].split(" ")
    if line0Split[0] == "seeds:":
        seeds = [range(int(line0Split[i]), int(line0Split[i]) + int(line0Split[i+1])) for i in range(1, len(line0Split[1:]), 2)] # now storing ranges

    else:
        maps.append(AOCmap())
        for line in lines[1:]:
            maps[mapIndex].add(line.split(" "))

        mapIndex += 1

print(seeds)
print(len(maps))

for mapO in maps:
    print()
    seeds = mapO.transform(seeds)
    # for i in range(len(seeds)):
    #     newNumber = mapO.transform(seeds[i])
    #     # print(newNumber)
    #     seeds[i] = newNumber
    # print(seeds)

    # print(seeds)
    seeds.sort(key = lambda a: a.start)
    # print(seeds)
    i = 0
    while i < len(seeds)-1:
        if seeds[i].stop == seeds[i+1].start:
            seeds[i] = range(seeds[i].start, seeds[i+1].stop)
            del seeds[i+1]
        else:
            i += 1
    # for i in range(len(seeds)-1):
    #     if seeds[i].stop == seeds[i+1].start:
    #         newSeeds.append(range(seeds[i].start, seeds[i+1].stop))
    #     else:
    #         newSeeds.append(seeds[i])
    #         if i == len(seeds) - 2:
    #             newSeeds.append(seeds[i+1])

    # print(seeds)

print(seeds)
# print(min(seeds, key=lambda a: a.start))
print(seeds[0].start)
