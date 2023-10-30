f = open("Input.txt", "r")
#print(f.read())
x = f.read().split("\n")
print(x)

horizontal = 0
depth = 0
aim = 0

for i in x:
    arr = i.split(" ")
    if arr[0] == "forward":
        horizontal += int(arr[1])
        depth += aim*int(arr[1])
    elif arr[0] == "up":
        aim -= int(arr[1])
    elif arr[0] == "down":
        aim += int(arr[1])
    else:
        print("oops")

print (horizontal)
print(depth)
print(horizontal*depth)
