f = open("input.txt", "r")
arr2d = [[j for j in i] for i in f.read().split("\n")]
print(arr2d)

start = (index := max([i if "S" in arr2d[i] else -1 for i in range(len(arr2d))]), arr2d[index].index("S"))

print(start)

def search(pos, count):
    print(f"Search path: searching {pos}")
    if min(pos) < 0 or max(pos) > max(len(arr2d), len(arr2d[0])):
        print(pos, "out of bounds")
        return 0

    if isinstance(arr2d[pos[0]][pos[1]], int):
        return count
    else:
        pipe = arr2d[pos[0]][pos[1]]
        print(pipe)
        arr2d[pos[0]][pos[1]] = count + 1
        if pipe == "|":
            num1 = search((pos[0] + 1, pos[1]), count + 1)
            num2 = search((pos[0] - 1, pos[1]), count + 1)
            return max(num1, num2)
        elif pipe == "-":
            num1 = search((pos[0], pos[1] + 1), count + 1)
            num2 = search((pos[0], pos[1] + 1), count + 1)
            return max(num1, num2)
        elif pipe == "L":
            num1 = search((pos[0] - 1, pos[1]), count + 1)
            num2 = search((pos[0], pos[1] + 1), count + 1)
            return max(num1, num2)
        elif pipe == "J":
            num1 = search((pos[0] - 1, pos[1]), count + 1)
            num2 = search((pos[0], pos[1] - 1), count + 1)
            return max(num1, num2)
        elif pipe == "7":
            num1 = search((pos[0] + 1, pos[1]), count + 1)
            num2 = search((pos[0], pos[1] - 1), count + 1)
            return max(num1, num2)
        elif pipe == "F":
            num1 = search((pos[0] + 1, pos[1]), count + 1)
            num2 = search((pos[0], pos[1] + 1), count + 1)
            return max(num1, num2)
        elif pipe == "S":
            nums = []
            if (next := arr2d[pos[0] - 1][pos[1]]) == "|" or next == "7" or next == "F":
                nums.append(search((pos[0] - 1, pos[1]), count + 1))
            if (next := arr2d[pos[0] + 1][pos[1]]) == "|" or next == "L" or next == "J":
                nums.append(search((pos[0] + 1, pos[1]), count + 1))
            if (next := arr2d[pos[0]][pos[1] - 1]) == "-" or next == "L" or next == "F":
                nums.append(search((pos[0], pos[1] - 1), count + 1))
            if (next := arr2d[pos[0]][pos[1] + 1]) == "-" or next == "7" or next == "J":
                nums.append(search((pos[0], pos[1] + 1), count + 1))

            print(nums)
            return max(nums)


def searchCorrect(start):
    queue = []

    queue.append(start)
    count = 0

    while len(queue) != 0:
        pos = queue.pop(0)
        # print(f"Searching {pos}")

        if isinstance(arr2d[pos[0]][pos[1]], int):
            continue

        pipe = arr2d[pos[0]][pos[1]]
        arr2d[pos[0]][pos[1]] = count

        if pipe == "|":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0] - 1, pos[1]))
            count += 1
        elif pipe == "-":
            queue.append((pos[0], pos[1] + 1))
            queue.append((pos[0], pos[1] - 1))
            count += 1
        elif pipe == "L":
            queue.append((pos[0] - 1, pos[1]))
            queue.append((pos[0], pos[1] + 1))
            count += 1
        elif pipe == "J":
            queue.append((pos[0] - 1, pos[1]))
            queue.append((pos[0], pos[1] - 1))
            count += 1
        elif pipe == "7":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0], pos[1] - 1))
            count += 1
        elif pipe == "F":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0], pos[1] + 1))
            count += 1
        elif pipe == "S":
            if (next := arr2d[pos[0] - 1][pos[1]]) == "|" or next == "7" or next == "F":
                queue.append((pos[0] - 1, pos[1]))
            if (next := arr2d[pos[0] + 1][pos[1]]) == "|" or next == "L" or next == "J":
                queue.append((pos[0] + 1, pos[1]))
            if (next := arr2d[pos[0]][pos[1] - 1]) == "-" or next == "L" or next == "F":
                queue.append((pos[0], pos[1] - 1))
            if (next := arr2d[pos[0]][pos[1] + 1]) == "-" or next == "7" or next == "J":
                queue.append((pos[0], pos[1] + 1))
            
            count += 1


    return count




# print(arr2d)

# print(search(start, -1))
print(searchCorrect(start)/2)

# for line in arr2d:
#     print(line)
# print(arr2d)



def searchArea(pos):
    # print(f"Search path: searching {pos}")
    if min(pos) < 0 or max(pos) > max(len(arr2d), len(arr2d[0])):
        print(pos, "out of bounds")
        return 0

    if isinstance(arr2d[pos[0]][pos[1]], int):
        return
    else:
        pipe = arr2d[pos[0]][pos[1]]
        print(pipe)
        arr2d[pos[0]][pos[1]] = -1
        if pipe == "|":
            search((pos[0] + 1, pos[1]))
            search((pos[0] - 1, pos[1]))
        elif pipe == "-":
            search((pos[0], pos[1] + 1))
            search((pos[0], pos[1] + 1))
        elif pipe == "L":
            search((pos[0] - 1, pos[1]))
            search((pos[0], pos[1] + 1))
        elif pipe == "J":
            search((pos[0] - 1, pos[1]))
            search((pos[0], pos[1] - 1))
        elif pipe == "7":
            search((pos[0] + 1, pos[1]))
            search((pos[0], pos[1] - 1))
        elif pipe == "F":
            search((pos[0] + 1, pos[1]))
            search((pos[0], pos[1] + 1))
        elif pipe == "S":
            if (next := arr2d[pos[0] - 1][pos[1]]) == "|" or next == "7" or next == "F":
                search((pos[0] - 1, pos[1]))
            if (next := arr2d[pos[0] + 1][pos[1]]) == "|" or next == "L" or next == "J":
                search((pos[0] + 1, pos[1]))
            if (next := arr2d[pos[0]][pos[1] - 1]) == "-" or next == "L" or next == "F":
                search((pos[0], pos[1] - 1))
            if (next := arr2d[pos[0]][pos[1] + 1]) == "-" or next == "7" or next == "J":
                search((pos[0], pos[1] + 1))


def betterSearchArea(start):
    queue = []

    outside = False
    queue.append(start)
    pipes = 0

    while len(queue) != 0:
        pos = queue.pop(0)
        # print(f"Searching {pos}")
        if min(pos) < 0 or max(pos) > max(len(arr2d), len(arr2d[0])):
            print(pos, "out of bounds")
            outside = True
            continue

        if isinstance(arr2d[pos[0]][pos[1]], int):
            continue


        pipe = arr2d[pos[0]][pos[1]]
        arr2d[pos[0]][pos[1]] = -1
        pipes += 1

        

        if pipe == "|":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0] - 1, pos[1]))
        elif pipe == "-":
            queue.append((pos[0], pos[1] + 1))
            queue.append((pos[0], pos[1] - 1))
        elif pipe == "L":
            queue.append((pos[0] - 1, pos[1]))
            queue.append((pos[0], pos[1] + 1))
        elif pipe == "J":
            queue.append((pos[0] - 1, pos[1]))
            queue.append((pos[0], pos[1] - 1))
        elif pipe == "7":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0], pos[1] - 1))
        elif pipe == "F":
            queue.append((pos[0] + 1, pos[1]))
            queue.append((pos[0], pos[1] + 1))
        elif pipe == "S":
            if (next := arr2d[pos[0] - 1][pos[1]]) == "|" or next == "7" or next == "F":
                queue.append((pos[0] - 1, pos[1]))
            if (next := arr2d[pos[0] + 1][pos[1]]) == "|" or next == "L" or next == "J":
                queue.append((pos[0] + 1, pos[1]))
            if (next := arr2d[pos[0]][pos[1] - 1]) == "-" or next == "L" or next == "F":
                queue.append((pos[0], pos[1] - 1))
            if (next := arr2d[pos[0]][pos[1] + 1]) == "-" or next == "7" or next == "J":
                queue.append((pos[0], pos[1] + 1))

    if not outside:
        return pipes


