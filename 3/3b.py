list = open("data.txt").read().splitlines()
list1 = list
list2 = list

lineLen = len(list[0])

oxNum = ''
coNum = ''

def countOxBit(index):
    count0 = 0
    count1 = 0
    for line in list1:
            if int(line[index]) == 0:
                count0 += 1
            elif int(line[index]) == 1: 
                count1 += 1
    return int(count1 >= count0)

def countCoBit(index):
    count0 = 0
    count1 = 0
    for line in list2:
            if int(line[index]) == 0:
                count0 += 1
            elif int(line[index]) == 1: 
                count1 += 1
    return int(count1 < count0)

def filterList(index, bit, newList): 
    newerList = []
    if len(newList) == 1: 
        return newList
    for line in newList: 
        if int(line[index]) == bit:
            newerList.append(line)
    return newerList

for n in range(lineLen):
    if len(list1) == 1:
        break
    countResult = countOxBit(n)
    list1 = filterList(n, countResult, list1)

for n in range(lineLen):
    if len(list2) == 1:
        break
    countResult = countCoBit(n)
    list2 = filterList(n, countResult, list2)


print(int(list1[0], 2))
print(int(list2[0], 2))

print("result: ", int(list1[0], 2) * int(list2[0], 2))
