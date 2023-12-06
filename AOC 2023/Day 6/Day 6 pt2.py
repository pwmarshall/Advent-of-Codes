f = open("input2.txt", "r")
#print(f.read())
lines = f.read().split("\n")
print(lines)
time = int(lines[0].split(" ")[1])
maxDistance = int(lines[1].split(" ")[1])

print(time)
print(maxDistance)


ways = 0
for hold in range(time):
    distance = (time-hold)*hold

    if distance > maxDistance:
        ways += 1

print(ways)
