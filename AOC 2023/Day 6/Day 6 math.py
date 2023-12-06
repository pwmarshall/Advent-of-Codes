import math

f = open("input2.txt", "r")
#print(f.read())
lines = f.read().split("\n")
print(lines)
time = int(lines[0].split(" ")[1])
maxDistance = int(lines[1].split(" ")[1])

print(time)
print(maxDistance)


holds = math.ceil((time + math.sqrt(time**2-4*maxDistance))/2) - math.ceil((time - math.sqrt(time**2-4*maxDistance))/2)

print(holds)