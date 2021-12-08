import math
list = open("data.txt").read().splitlines()

for x in range(len(list)): 
    list[x] = list[x].split(" -> ")
    for y in range(len(list[x])):
        list[x][y] = list[x][y].split(",")

hitCoords = {}

for set in list: 

    x1 = int(set[0][0])
    y1 = int(set[0][1])
    x2 = int(set[1][0])
    y2 = int(set[1][1])

    deltaX = (((x2 - x1)/abs(max(abs((x2 - x1)), 1))))
    deltaY = (((y2 - y1)/abs(max(abs((y2 - y1)), 1))))
    currX = x1
    currY = y1

    for i in range(max((abs(x2 - x1) + 1), (abs(y2 - y1) + 1))): 
            current = hitCoords.get("{},{}".format(currX,currY), None)
            if current == None: 
                hitCoords["{},{}".format(currX,currY)] = 1
            else: 
                hitCoords["{},{}".format(currX,currY)] += 1
            currX = int(currX + deltaX)
            currY = int(currY + deltaY)

countSmoke = 0
for key in hitCoords: 
    if hitCoords[key] > 1:
        countSmoke+=1
        print(key)

print("result: ", countSmoke)