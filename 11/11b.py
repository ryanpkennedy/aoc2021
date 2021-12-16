list = open('data.txt').read().splitlines()

for x in range(len(list)):
    list[x] = [int(num) for num in list[x]]

coordStack = []
flashCount = 0

def flash(n,m):
    # diagonal top left
    if (not n == 0) and (not m == 0):
        list[n-1][m-1] += 1
        coordStack.append([n-1, m-1])

    # diagonal top right
    if (not n == 0) and (not m == (len(list[n]) - 1)):
        list[n-1][m+1] += 1
        coordStack.append([n-1, m+1])

    # diagonal bottom left
    if (not n == (len(list) - 1)) and (not m == 0):
        list[n+1][m-1] += 1
        coordStack.append([n+1, m-1])

    # diagonal bottom right
    if (not n == (len(list) - 1)) and (not m == (len(list[n]) - 1)):
        list[n+1][m+1] += 1
        coordStack.append([n+1, m+1])

    # top
    if not n == 0:
        list[n-1][m] += 1
        coordStack.append([n-1, m])

    # bottom
    if not n == (len(list) -1):
        list[n+1][m] += 1
        coordStack.append([n+1, m])

    # left
    if not m == 0:
        list[n][m-1] += 1
        coordStack.append([n, m-1])

    # right
    if not m == (len(list[n]) - 1):
        list[n][m+1] += 1
        coordStack.append([n, m+1])


def incrementAll():
    for n in range(len(list)):
        for m in range(len(list[n])):
                list[n][m] += 1
                if list[n][m] > 9:
                    coordStack.append([n,m])

def runFlashes():
    global flashCount
    while len(coordStack) > 0:
        current = coordStack.pop()
        n = int(current[0])
        m = int(current[1])
        if list[n][m] > 9:
            if not str([n,m]) in flashSet:
                flashSet.add(str([n,m]))
                flashCount+=1
                flash(n,m)

def cleanup():
    for n in range(len(list)):
        for m in range(len(list[n])):
            if list[n][m] > 9:
                list[n][m] = 0


def printMap():
    for n in list:
        print(n)
    print('flash count:', flashCount)


for _ in range(1000):
    flashSet = set()
    incrementAll()
    # print('after step', _+1)
    runFlashes()
    cleanup()
    # printMap()
    # print('\n')
    if len(flashSet) == 100:
        print('round:', _ + 1)
        exit()

