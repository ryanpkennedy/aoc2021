list = open('data.txt').read().split()

for x in range(len(list)):
    list[x] = [i for i in list[x]]

minArray = []

for n in range(len(list)):
    for m in range(len(list[0])):
        current = int(list[n][m])
        top = 9
        bottom = 9
        left = 9
        right = 9
        if n > 0:
            top = int(list[n-1][m])
        if n < (len(list) -1):
            bottom = int(list[n+1][m])
        if m > 0:
            left = int(list[n][m-1])
        if m < (len(list[0])-1):
            right = int(list[n][m+1])
        if current < left and current < right and current < top and current < bottom:
            minArray.append([n,m])

countArray = []

for testCase in range(len(minArray)):

    basinArray = []
    basinSet = set()

    def countBasin(coords):
        current = int(list[coords[0]][coords[1]])
        top = 9
        bottom = 9
        left = 9
        right = 9
        
        if coords[0] > 0:
            top = int(list[coords[0] - 1][coords[1]])
            if top > current and (not top == 9):
                basinArray.append([coords[0]-1,coords[1]])

        if coords[0] < (len(list) - 1):
            bottom = int(list[coords[0] + 1][coords[1]])
            if bottom > current and (not bottom == 9):
                basinArray.append([coords[0] + 1,coords[1]])

        if coords[1] > 0:
            left = int(list[coords[0]][coords[1] - 1])
            if left > current and (not left == 9):
                basinArray.append([coords[0],coords[1] - 1])

        if coords[1] < (len(list[0]) - 1):
            right = int(list[coords[0]][coords[1] + 1])
            if right > current and (not right == 9):
                basinArray.append([coords[0],coords[1] + 1])
        

    basinArray.append(minArray[testCase])

    while len(basinArray) > 0:
        nextCase = basinArray.pop()
        basinSet.add(str(nextCase))
        countBasin(nextCase)

    count = 0
    for coord in basinSet:
        count+=1

    countArray.append(count)

countArray.sort()

result = countArray[len(countArray)-1] * countArray[len(countArray)-2] * countArray[len(countArray)-3]
print(result)