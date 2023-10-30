
f = open("Day 3 Input.txt", "r")
#print(f.read())
arr = f.read().split("\n")
arr.pop()

for i in range(len(arr)):
    arr[i] = arr[i].split(" ")

#print(arr)

x = 0

count = 0

for y in range(len(arr)):
    if(y % 2 == 0):
        #print(y)
        #print(x)
        #print(arr[y][x])

        if(arr[y][x] == "#"):
            count += 1

        x += 1

        if(x >= len(arr[0])):
            x %= len(arr[0])

print(count)


#1,1 = 67
#3,1 = 211
#5,1 = 77
#7,1 = 89
#1,2 = 37
