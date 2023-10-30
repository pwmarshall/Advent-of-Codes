
f = open("Day 5 Input.txt", "r")
#print(f.read())
arr = f.read().split("\n")
arr.pop()

largest = 0
seats = []

for l in arr:
    working = l[:7]
    working = working.replace("F", "0")
    working = working.replace("B", "1")

    row = int(working, 2)
    #print(row)

    working = l[-3:]
    working = working.replace("L", "0")
    working = working.replace("R", "1")

    column = int(working, 2)
    #print(column)

    ID = (row * 8) + column

    #part 1
#    if ID > largest:
#        largest = ID

    seats.append(ID)

#print(largest)

seats.sort()
#print(seats)

last = 0
next = 0
missing = []

for seat in seats:
    if last != seat - 1:
        missing.append(seat-1)

    last = seat

print(missing)
