
f = open("Day 6 Input.txt", "r")
#print(f.read())
arr = f.read().split("\n\n")


totalCount = 0

for i in range(len(arr)):  #for each group
    arr[i] = arr[i].split("\n")
    if(i == len(arr) -1):
        arr[i].pop()        #get rid of new line at bottom of file

    #print(arr[i])


#part 1


    groupCount = 0
    arrYes = []

#    for j in range(len(arr[i])): #for each person in group
#        for yes in arr[i][j]: #for each answer of yes


            #if yes not in arrYes:
                #groupCount += 1
                #arrYes.append(yes)



#    print(groupCount)
#    totalCount += groupCount


#part 2

    print("\n" + arr[i][0])

    for yes in arr[i][0]: #go though 1st persons answers
        print(yes)
        yesCount = 0
        for j in range(len(arr[i])): #check if everyone else ansered

            #print(arr[i][j])

            if yes in arr[i][j]: #if 1 person answered
                yesCount += 1 #count as one answering

        print(yesCount)
        print(len(arr[i]))

        if yesCount == len(arr[i]): #if i counted everyone answering the same
            print("Group answered")
            groupCount += 1 #group has a anwser

    print(groupCount)

    totalCount += groupCount

print(totalCount)
