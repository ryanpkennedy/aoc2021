list = open("data.txt").read().splitlines()

lineLen = len(list[0])

count0 = [0 for x in range(lineLen)]
count1 = [0 for x in range(lineLen)]
gammaNum = ''
epsilonNum = ''

for line in list:
    for x in range(lineLen):
        if int(line[x]) == 0:
            count0[x] += 1
        elif int(line[x]) == 1: 
            count1[x] += 1

for x in range(lineLen):
    gammaNum +=  str(int(count1[x] > count0[x]))
    epsilonNum += str(int(count0[x] > count1[x]))

    
print("count0: ", count0, "\n", "count1: ", count1, "\n")

print("gammaNum: ", int(gammaNum,2))
print("epsilonNum: ", int(epsilonNum,2))

print("result: ", int(gammaNum,2) * int(epsilonNum,2))