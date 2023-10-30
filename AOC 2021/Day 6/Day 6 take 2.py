f = open("Input.txt", "r")
#print(f.read())
x = f.read().split(",")
print(x)

#setup
fishes = []
for i in x:
    fishes.append(int(i))

daysLeft = [0,0,0,0,0,0,0,0,0]

for fish in fishes:
    daysLeft[fish] += 1

print(daysLeft)

tempDaysLeft = []
for i in range(256):
    tempDaysLeft = [daysLeft[1],daysLeft[2],daysLeft[3],daysLeft[4],daysLeft[5],daysLeft[6],daysLeft[7]+daysLeft[0],daysLeft[8],daysLeft[0]]
    daysLeft = tempDaysLeft
    print(daysLeft)


# print(daysLeft)

sum = 0
for fish in daysLeft:
    sum += fish

print(sum)
