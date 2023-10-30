import math
f = open("Input.txt", "r")
#print(f.read())
x = f.read().split(",")
print(x)


working = []
for number in x:
    working.append(int(number))



count = []
print(max(working))
sum = 0
sums=[]
for i in range(max(working)+1):
    answer = i

    sum = 0
    for pos in working:
        sum += 1/2*abs(pos - answer)*(abs(pos - answer)+1)

    print(sum)
    sums.append(sum)

print(min(sums))
# average = 0
# for pos in working:
#     average += pos
#
# average = math.floor(average/len(working))
# print(average)
#
# # print(count)
# #
# # print(max(count))
# # print(count.index(max(count)))
# # answer = count.index(max(count))
#
# for i in range(-5,5):
#     answer = average + i
#
#     sum = 0
#     for pos in working:
#         sum += abs(pos - answer)
#
#     print(sum)