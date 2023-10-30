import time

f = open("Day 7 Input.txt", "r")
#print(f.read())
arrRules = f.read().split("\n") #arr of all the rules
arrRules.pop()

#part 1

#count = 0
#arrHoldBags = []
#allBags = []
#moreBags = "true"

#for rule in arrRules:
#    if " shiny gold" in rule: #add space in front to not get the descriptor of the bag
#        count += 1
#        print(rule)
#        arrHoldBags.append(rule.split(" bags contain")[0])
#        allBags.append(rule.split(" bags contain")[0])



#print(arrHoldBags)
#print(count)


#while moreBags == "true":
#    tempHoldBags = arrHoldBags
#    arrHoldBags = []
#    for bag in tempHoldBags:
#        print(bag)
#        for rule in arrRules:
#            if " " + bag in rule and rule.split(" bags contain")[0] not in allBags:
#                count += 1
#                print(rule)
#                arrHoldBags.append(rule.split(" bags contain")[0])
#                allBags.append(rule.split(" bags contain")[0])


#        print(arrHoldBags)
#        print(count)

#    if arrHoldBags == []:
#        moreBags = "false"

#    time.sleep(3)

#print("done")
#print(count)

colors = []

for rule in arrRules:
    if "shiny gold" == rule.split(" bags contain")[0]:
        print(rule)
        for color in rule.split(" bags contain ")[1].split(", "):
            color = color.split("bag").pop(0)
            #print(color)
            colors.append(color)
            #print(colors)

print(colors)
