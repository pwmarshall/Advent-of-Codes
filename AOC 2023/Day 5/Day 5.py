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

    def transform(self, number):
        # print(f"transforming {number}")
        for arr in self.ranges:
            # print(f"if {number} in: {arr[0]}, add {arr[1]}")
            # print(number in arr[0])
            if number in arr[0]:
                newNumber = number + arr[1]
                return newNumber
            
        return number




maps = []
seeds = []
mapIndex = 0

for cat in cats:
    
    print(cat)
    lines = cat.split("\n")

    if lines[0].split(" ")[0] == "seeds:":
        seeds = [int(i) for i in lines[0].split(" ")[1:]]

    else:
        maps.append(AOCmap())
        for line in lines[1:]:
            maps[mapIndex].add(line.split(" "))

        mapIndex += 1

print(seeds)
print(maps)
print(len(maps))

for mapO in maps:
    print()
    for i in range(len(seeds)):
        newNumber = mapO.transform(seeds[i])
        # print(newNumber)
        seeds[i] = newNumber
    print(seeds)

print(min(seeds))
