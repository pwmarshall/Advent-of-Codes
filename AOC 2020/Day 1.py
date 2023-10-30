
f = open("Day 1 Input.txt", "r")
#print(f.read())
x = f.read().split("\n")
x.pop()
#print(x)

#part 1

#for number in x:
#    opposite = 2020 - int(number)
#    #print(opposite)
#    if str(opposite) in x:
#        print(number)
#        print(opposite)

#part 2

for number1 in x:
    for number2 in x:
        for number3 in x:
            if int(number1) + int(number2) + int(number3) == 2020:
                print(number1)
                print(number2)
                print(number3)



f.close()
