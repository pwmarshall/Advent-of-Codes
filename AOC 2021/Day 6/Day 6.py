f = open("Input.txt", "r")
#print(f.read())
x = f.read().split(",")
print(x)

#setup
fishes = []
for i in x:
    fishes.append(int(i))

print(fishes)

for i in range(256):
    tempFishes = []
    for fish in fishes:
        if(fish != 0):
            tempFishes.append(fish-1)
        else:
            tempFishes.append(6)
            tempFishes.append(8)

    fishes = tempFishes

print(len(fishes))
