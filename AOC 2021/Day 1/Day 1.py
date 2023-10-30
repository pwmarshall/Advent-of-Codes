f = open("Input.txt", "r")
#print(f.read())
x = f.read().split("\n")
print(x)

#part 2:
lastNumber = 0
lastlastNumber = 0
newX = []

for i in x:
    if int(lastNumber) == 0:
        lastNumber = i
    elif int(lastlastNumber) ==0:
        lastlastNumber = lastNumber
        lastNumber = i
    else:
        newX.append(int(lastNumber) + int(lastlastNumber) + int(i))
        lastlastNumber = lastNumber
        lastNumber = i

print(newX)

#part 1:
lastNumber = 1000
count = 0
for i in newX: #x:
    if int(i) > int(lastNumber):
        count += 1
        lastNumber = i
    else:
        lastNumber = i


print(count)