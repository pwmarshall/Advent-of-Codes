f = open("Input.txt", "r")
# print(f.read())
x = f.read().split("\n")
print(x)


#part 1:
# gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# for count in range(12):
#     print(count)
#     count1 = 0
#     count0 = 0
#     for bits in x:
#         if bits[count] == "0":
#             count0 += 1
#         else:
#             count1 += 1
#
#     print(count1)
#     print(count0)
#
#     if count0 > count1:
#         gamma[count] = 0
#         epsilon[count] = 1
#     else:
#         gamma[count] = 1
#         epsilon[count] = 0
#
# print(gamma)
# print(epsilon)

#part 2:

oxygen = x

for count in range(12):
    print(count)
    count1 = 0
    count0 = 0
    for bits in oxygen:
        if bits[count] == "0":
            count0 += 1
        else:
            count1 += 1

    #print(count1)
    #print(count0)
    removeBits = []

    if count0 > count1:
        for bits in oxygen:
            if bits[count] == "0":
                #oxygen.remove(bits)
                removeBits.append(bits)

    elif count1 > count0:
        for bits in oxygen:
            if bits[count] == "1":
                #oxygen.remove(bits)
                removeBits.append(bits)

    elif count1 == count0:
        for bits in oxygen:
            if bits[count] == "1":
                #oxygen.remove(bits)
                removeBits.append(bits)

    for badBit in removeBits:
        oxygen.remove(badBit)

    #print(oxygen)
    if len(oxygen) == 1:
        break

print(oxygen)