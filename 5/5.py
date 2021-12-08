import math
list = open("data.txt").read().splitlines()

for x in range(len(list)): 
    list[x] = list[x].split(" -> ")
    for y in range(len(list[x])):
        list[x][y] = list[x][y].split(",")

max = 9

hitCoords = {}

for set in list: 
    print("current set: ", set)
    x1 = int(set[0][0])
    y1 = int(set[0][1])
    x2 = int(set[1][0])
    y2 = int(set[1][1])
    # print("x1: ", x1, "\ny1: ", y1, "\nx2: ", x2, "\ny2: ", y2)
    if x1 != x2 and y1 != y2:
        print("not straight line")
        continue
    for x in range(abs(x2 - x1) + 1): 
        for y in range(abs(y2 - y1) + 1):
            currX = min(x1,x2) + x
            currY = min(y1,y2) + y
            current = hitCoords.get("{},{}".format(currX,currY), None)
            if current == None: 
                hitCoords["{},{}".format(currX,currY)] = 1
            else: 
                hitCoords["{},{}".format(currX,currY)] += 1

countSmoke = 0
for key in hitCoords: 
    if hitCoords[key] > 1:
        countSmoke+=1
        print(key)

print("result: ", countSmoke)