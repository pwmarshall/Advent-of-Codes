f = open("input.txt", "r")
strings = f.read().split(",")
print(strings)


# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.


def hash(string):
    hashValue = 0
    for character in string:
        hashValue += ord(character)
        hashValue *= 17
        hashValue %= 256

    return hashValue

print(sum([hash(i) for i in strings]))


table = {}
for i in range(256):
    table[i] = []

intructions = [i.split("=") if "=" in i else i.split("-") for i in strings]
print(intructions)

for label, focal in intructions:
    h = hash(label)
    # print(label)
    labels = [table[h][i][0] for i in range(len(table[h]))]
    # print(labels)

    if focal == "":
        if label in labels:
            table[h].pop(labels.index(label))
    else:
        if label in labels:
            table[h][labels.index(label)][1] = focal
        else:
            table[h].append([label, focal])
            
print(table)

sumFocusingPower = 0
for i in range(256):
    # print(i, "i")
    for j in range(len(table[i])):
        # print(j, "j")
        focusingPower = (i+1) * (j+1) * int(table[i][j][1])
        # print(focusingPower, "power")
        sumFocusingPower += focusingPower
        

print(sumFocusingPower)