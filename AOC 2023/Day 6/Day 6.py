f = open("input.txt", "r")
#print(f.read())
lines = f.read().split("\n")
print(lines)
times = [int(i) for i in lines[0].split(" ")[1:]]
distances = [int(i) for i in lines[1].split(" ")[1:]]

print(times)
print(distances)

product = 1

for i in range(len(times)):
    time = times[i]
    maxDistance = distances[i]
    ways = 0
    for hold in range(time):
        distance = (time-hold)*hold

        if distance > maxDistance:
            ways += 1

    product *= ways

print(product)