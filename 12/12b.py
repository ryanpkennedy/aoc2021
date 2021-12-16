import time

list = open('test3.txt').read().splitlines()

data = []
smallCount = 0

# create array of data 
for line in list:
    temp = line.split("-")
    connection = []
    for point in temp:
        connection.append(point)
    data.append(connection)

#create reverse paths as well
for x in range(len(data)):
    reverseConnection = [data[x][1], data[x][0]]
    data.append(reverseConnection)

results = []
finalPaths = []

#get starting paths
for point in data:
    if point[0] == 'start':
        path = []
        path.append(point[0])
        path.append(point[1])
        results.append(path)

def nextOptions(letter, array):
    options = []
    global smallCount
    for point in data:
        if point[0] == letter:
            if (point[1].lower() == point[1]) and (point[1] in array):
                if smallCount > 0 or point[1] == 'start':
                    continue
                else:
                    options.append(point[1])
            else:
                options.append(point[1])
    return options

def findNext(array):
    pathEnd = array[-1]
    optionalPaths = []
    optionalPoints = nextOptions(pathEnd, array)
    for i in optionalPoints:
        addPath = array + [i]
        optionalPaths.append(addPath)
    return optionalPaths

def countLower(array):
    lowerCount = []
    for i in array:
        if i.lower() == i:
            occurs = array.count(i)
            lowerCount.append(occurs)
    return lowerCount


while len(results) > 0:
    smallCount = 0
    # print('current paths:', results)
    nextPath = results.pop(0)
    lowerArray = countLower(nextPath)
    maxLower = max(lowerArray)
    if maxLower > 1:
        smallCount = 1
    if nextPath[-1] == 'end':
        finalPaths.append(nextPath)
    else:
        optionalPaths = findNext(nextPath)
        # print('for next path:', nextPath, '\noptional paths:',optionalPaths)
        for i in optionalPaths:
            results.append(i)

print(len(finalPaths))

#####################################################################################

    