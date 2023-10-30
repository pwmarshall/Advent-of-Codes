
f = open("Day 4 Input.txt", "r")
#print(f.read())
arr = f.read().split("\n\n")

count = 0

hclCorrect = ["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"]
eclCorrect = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for i in range(len(arr)):
    arr[i] = arr[i].split("\n")
    if(i == len(arr) -1):
        arr[i].pop()        #get rid of new line at bottom of file

    #print(arr[i])

#part 1

#    if(len(arr[i]) == 8):
#        count += 1
#
#    elif(len(arr[i]) == 7):
#        good = 0
#        for d in arr[i]:    #if d is never cid passport is good
#            if(d[:3] != "cid"):
#                good += 1
#
#        if(good == 7):
#            count += 1

#part 2

    good = 0
    hclGood = 0

    #print(i)

    for d in arr[i]:
        if(d[:3] == "byr"): #four digits; at least 1920 and at most 2002.
            if(len(d[4:]) == 4):
                if(int(d[4:]) >= 1920 and int(d[4:]) <= 2002):
                    good += 1
                    #print(d + " is good byr")
        elif(d[:3] == "iyr"): #four digits; at least 2010 and at most 2020.
            if(len(d[4:]) == 4):
                if(int(d[4:]) >= 2010 and int(d[4:]) <= 2020):
                    good += 1
                    #print(d + " is good iyr")
        elif(d[:3] == "eyr"): #four digits; at least 2020 and at most 2030
            if(len(d[4:]) == 4):
                if(int(d[4:]) >= 2020 and int(d[4:]) <= 2030):
                    good += 1
                    #print(d + " is good iyr")
        elif(d[:3] == "hgt"): #a number followed by either cm or in
            #print(d[4:-2])
            if(d[-2:] == "in"): #at least 59 and at most 76
                if(int(d[4:-2]) >= 59 and int(d[4:-2]) <= 76):
                    good += 1
                    #print(d + " is good hgt")
            elif(d[-2:] == "cm"): #at least 150 and at most 193
                if(int(d[4:-2]) >= 150 and int(d[4:-2]) <= 193):
                    good += 1
                    #print(d + " is good hgt")
        elif(d[:3] == "hcl"): #a "#" followed by exactly six characters 0-9 or a-f
            if(d[4:5] == "#" and len(d[5:]) == 6):
                #print(d[4:])
                for l in d[5:]:
                    #print(l)
                    if l in hclCorrect:
                        hclGood += 1

                if(hclGood == 6):
                    good += 1
                    #print(d + " is good hcl")
        elif(d[:3] == "ecl"): #exactly one of: amb blu brn gry grn hzl oth
            #print(d[4:])
            if(d[4:] in eclCorrect):
                good += 1
                #print(d + " is a good ecl")
        elif(d[:3] == "pid"): #a nine-digit number, including leading zeroes
            if(len(d[4:]) == 9):
                good += 1
                #print(d + " is a good pid")
        elif(d[:3] == "cid"): #doesnt matter
            pass

    if(good == 7):
        count += 1
        #print(arr[i])
        #print(i)

#print(arr)
print(count)
