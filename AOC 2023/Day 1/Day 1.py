debug = False

if debug:
    f = open("input2test.txt", "r")
else:
    f = open("input1.txt", "r")
#print(f.read())
x = f.read().split("\n")
print(x)

ints = ["0","1","2","3","4","5","6","7","8","9"]
sum = 0

# part 1
for line in x:
    firstInt = -1
    lastInt = -1
    for letter in line:
        if letter in ints:
            if firstInt == -1:
                firstInt = letter
            lastInt = letter

    sum += int(firstInt + lastInt)

# print(sum)

sum = 0
compare1 = []
compare2 = []

# part 2

allInts = ["1","2","3","4","5","6","7","8","9", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in x:
    firstInt = -1
    firstIndex = 10000
    lastInt = -1
    lastIndex = -1
    for i in range(18):
        workingLine = line
        index = 0
        cutIndex = 0
        while allInts[i] in workingLine:
            index = workingLine.index(allInts[i]) + cutIndex
            if debug:
                print(workingLine)
                print(allInts[i])
                print(index)
            number = (i % 9) + 1
            if firstIndex > index:
                firstIndex = index
                firstInt = str(number)

            if lastIndex < index:
                lastIndex = index
                lastInt = str(number)
            
            workingLine = workingLine[index + 1:]
            cutIndex = index + 1 + cutIndex
            

    # for letter in line:
    #     if letter in ints:
    #         index = line.index(letter)

    #         print(letter)
    #         print(index)
    #         print(firstIndex)
    #         print(lastIndex)
    #         if firstIndex > index:
    #             firstIndex = index
    #             firstInt = letter
 
    #         if lastIndex < index:
    #             lastIndex = index
    #             lastInt = letter

    if debug:
        print(line)
        print(firstInt + lastInt)
    
    sum += int(firstInt + lastInt)
    compare1.append(int(firstInt + lastInt))

print(sum)
        



import regex as re

input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

numbers_string = '|'.join(numbers)

if __name__ == "__main__":
    sum = 0

    for line in x:
        # overlapped=True is vital here!
        digits = re.findall(rf"(\d|{numbers_string})", line, overlapped=True)
        first = digits[0]
        last = digits[-1]

        #print(f"{line} = {first} {last}")

        if len(first) > 1:
            first = numbers.index(first) + 1

        if len(last) > 1:
            last = numbers.index(last) + 1

        linedigits = f"{first}{last}"
        sum += int(linedigits)
        if debug:
            print(linedigits)
        compare2.append(int(linedigits))

    print(f"Result: {sum}")


for i in range(len(compare1)):
    if compare1[i] != compare2[i]:
        print(i)