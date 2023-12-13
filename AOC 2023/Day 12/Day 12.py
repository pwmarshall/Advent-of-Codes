import math
f = open("inputTest.txt", "r")
input = [i.split(" ") for i in f.read().split("\n")]

print(input)
sumed = 0

for line in input:
    spl = line[0].split(".")
    nums = [int(i) for i in line[1].split(",")]
    lengs = [leng for i in spl if (leng:= len(i)) != 0]

    print(nums)
    print(lengs)

    if len(nums) == len(lengs):
        sumed += (out:= max(sum([com for i in range(len(nums)) if (com:= math.comb(lengs[i], nums[i])) != 1]), 1))
        print(out)
    else:
        together = ".".join(spl)
        print(together, nums)
        target = ".".join(["#"*num for num in nums])
        print(target)
        if len(together) == len(target):
            sumed += 1
            print(1)
        elif len(together) < len(target):
            print("REEE")
        else:
            search = target.split(".")
            indexes = [together.find(i) for i in search]
            print(indexes)

            index = indexes[0]
            if index != -1:
                target = "."*index + target
                print(target)
                
                if len(together) == len(target):
                    sumed += 1
                    print(1)
                else:
                    i = 0
                    matching = True
                    while (matching):
                        if (together[i] == "#" and together[i] != target[i]) or (together[i] == "?" and target[i] == "#"):
                            matching = False
                            break

                        i += 1

                    print(f"Together and target matching until index {i}")
                    # print(math.comb(len(together) - i, len(target) - i + len(target.split("."))))
                    # print(math.comb(7 - 2, 3))
                    # print(math.comb(len(together) - i - ))
                    print(math.comb(2+3-1, 3-1), math.comb(1+3-1, 3-1))
                    length = len(together) - i
                    print(math.comb(length ))
                    # good until i


print(sumed)