import time

list = open('data.txt').read().splitlines()

data = []

# create array of data 
for line in list:
    temp = line.split("-")
    connection = []
    for point in temp:
        connection.append(point)
    data.append(connection)

# print(data, '\n')


#create reverse paths as well
for x in range(len(data)):
    reverseConnection = [data[x][1], data[x][0]]
    data.append(reverseConnection)

results = []
finalPaths = []

for point in data:
    if point[0] == 'start':
        path = []
        path.append(point[0])
        path.append(point[1])
        results.append(path)

def nextOptions(letter, array):
    options = []
    for point in data:
        if point[0] == letter:
            if (point[1].lower() == point[1]) and (point[1] in array):
                continue
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


# print(results)

while len(results) > 0:
    # print('current paths:', results)
    nextPath = results.pop(0)
    if nextPath[-1] == 'end':
        finalPaths.append(nextPath)
    else:
        optionalPaths = findNext(nextPath)
        # print('for next path:', nextPath, '\noptional paths:',optionalPaths)
        for i in optionalPaths:
            results.append(i)
    # print('\n')
    # time.sleep(0.5)

# print(finalPaths)
# for i in finalPaths:
#     print(i)

print(len(finalPaths))
exit()

#####################################################################################

    