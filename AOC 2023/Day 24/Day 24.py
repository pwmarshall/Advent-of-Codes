fText = open("input.txt", "r").read()
posvel = [[[int(j) for j in i.split(" @ ")[0].split(", ")], [int(j) for j in i.split(" @ ")[1].split(", ")]] for i in fText.split("\n")]

print(posvel)

# 44850 combinations to check

count = 0
minPos = 200000000000000
maxPos = 400000000000000

for i in range(len(posvel)-1):

    # general equation coefficents
    a1 = -1 * posvel[i][1][1]
    b1 = posvel[i][1][0]
    c1 = -1*(b1 * posvel[i][0][1] + a1 * posvel[i][0][0])

    for j in range(i + 1, len(posvel)):
        # print(f"combine {i}, and {j}")

        # general equation coefficents
        a2 = -1 * posvel[j][1][1]
        b2 = posvel[j][1][0]
        c2 = -1*(b2 * posvel[j][0][1] + a2 * posvel[j][0][0])

        eqBot = (a1*b2-a2*b1)
        if eqBot != 0:
            # https://www.cuemath.com/geometry/intersection-of-two-lines/
            intersection = ((b1*c2-b2*c1)/eqBot, (c1*a2-c2*a1)/eqBot) #(x,y)

            t1 = (intersection[0]-posvel[i][0][0])/posvel[i][1][0]
            t2 = (intersection[0]-posvel[j][0][0])/posvel[j][1][0]
            # print("t1 =", t1)
            if t1 < 0 or t2 < 0:
                # print("past")
                pass
            else:
                # print(intersection)
                if min(intersection) >= minPos and max(intersection) <= maxPos:
                    # print("inside")
                    count+=1
                # else:
                #     print("outside")

        # else:
            # print("Parallel")
        # print()
                    
print(count)