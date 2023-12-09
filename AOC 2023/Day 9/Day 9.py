f = open("input.txt", "r")
text = f.read().split("\n")
print(text)

lines = [[int(i) for i in j.split(" ")] for j in text]

print(lines)
sum1 = 0
sum2 = 0

for line in lines:

    arr2d = [line]
    while not all([i == 0 for i in arr2d[-1]]):
        arr2d.append([arr2d[-1][i+1] - arr2d[-1][i] for i in range(len(arr2d[-1]) - 1)])

    # print(arr2d)

    arr2d[-1].append(0)

    for i in range(len(arr2d)-2, -1, -1):
        arr2d[i].append(arr2d[i+1][-1] + arr2d[i][-1])

    # print(arr2d)
    sum1 += arr2d[0][-1]

    #part 2
    arr2d[-1].insert(0, 0)

    for i in range(len(arr2d)-2, -1, -1):
        arr2d[i].insert(0, - arr2d[i+1][0] + arr2d[i][0])

    print(arr2d)
    sum2 += arr2d[0][0]



print(sum1)
print(sum2)