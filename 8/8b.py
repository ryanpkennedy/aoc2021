list = open('data.txt').read().splitlines()
inputList = []
outputList = []
outputNums = []
testCase = 2

for x in range(len(list)):
    nextInput = list[x].split(" | ")
    inputList.append(nextInput)
    inputList[x] = inputList[x][0]
    inputList[x] = inputList[x].split(" ")

for x in range(len(list)):
    nextOutput = list[x].split(" | ")
    nextOutput = nextOutput[1]
    outputList.append(nextOutput)
    outputList[x] = outputList[x].split(" ")



def SortDigit(digit): 
    sortedDigit = ""
    return sortedDigit.join(sorted(digit))

for testCase in range(len(inputList)):
    codeDict = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
    }

    topLine = ""
    centerLine = ""
    upperLeft = ""
    bottomLeft = ""
    bottomRight = ""
    upperRight = ""

    def FindTopLine(dict):
        setOne = set(dict[1])
        setSeven = set(dict[7])
        topLineSet = setSeven - setOne
        global topLine
        for d in topLineSet:
            topLine = d

    def FindCenterLine(array):
        setA = set(array[0])
        setB = set(array[1])
        setC = set(array[2])
        setMiddle = setA.intersection(setB, setC)
        setOne = set(codeDict[1])
        setFour = set(codeDict[4])
        centerSet = setFour.intersection(setMiddle)
        upperLeftSet = setFour - setOne
        upperLeftSet = upperLeftSet - setMiddle
        global centerLine
        for d in centerSet:
            centerLine = d
        global upperLeft
        for d in upperLeftSet:
            upperLeft = d

    TwoThreeFive = []

    for digit in inputList[testCase]: 
        length = len(digit)
        if length == 2:
            codeDict[1] = SortDigit(digit)
        elif length == 3:
            codeDict[7] = SortDigit(digit)
        elif length == 4: 
            codeDict[4] = SortDigit(digit)
        elif length == 7: 
            codeDict[8] = SortDigit(digit)
        elif length == 5:
            TwoThreeFive.append(digit)

    def FindZero():
        setEight = set(codeDict[8])
        setCenter = set(centerLine)
        setZero = setEight - setCenter
        stringZero = ""
        stringZero = stringZero.join(setZero)
        codeDict[0] = SortDigit(stringZero)

    def FindFive(array):
        setA = set(array[0])
        setB = set(array[1])
        setC = set(array[2])
        stringFive = ""
        if upperLeft in setA:
            stringFive = stringFive.join(setA)
        elif upperLeft in setB:
            stringFive = stringFive.join(setB)
        elif upperLeft in setC:
            stringFive = stringFive.join(setC)
        codeDict[5] = SortDigit(stringFive)

    def FindBottomRight():
        setOne = set(codeDict[1])
        setFive = set(codeDict[5])
        setBottomRight = setFive.intersection(setOne)
        global bottomRight
        for d in setBottomRight:
            bottomRight = d

    def FindTwo(array):
        setA = set(array[0])
        setB = set(array[1])
        setC = set(array[2])
        stringTwo = ""
        if not bottomRight in setA:
            stringTwo = stringTwo.join(setA)
        elif not bottomRight in setB:
            stringTwo = stringTwo.join(setB)
        elif not bottomRight in setC:
            stringTwo = stringTwo.join(setC)
        codeDict[2] = SortDigit(stringTwo)

    def FindUpperRight():
        setOne = set(codeDict[1])
        setBottomRight = set(bottomRight)
        setUpperRight = setOne - setBottomRight
        global upperRight
        for d in setUpperRight:
            upperRight = d

    def FindSix():
        setEight = set(codeDict[8])
        setUpperRight = set(upperRight)
        setSix = setEight - setUpperRight
        stringSix = ""
        stringSix = stringSix.join(setSix)
        codeDict[6] = SortDigit(stringSix)
        
    def FindThree(array):
        setA = set(array[0])
        setB = set(array[1])
        setC = set(array[2])
        setTwo = set(codeDict[2])
        setFive = set(codeDict[5])
        stringThree = ""
        if (not setA == setTwo) and (not setA == setFive):
            stringThree = stringThree.join(setA)
        if (not setB == setTwo) and (not setB == setFive):
            stringThree = stringThree.join(setB)
        if (not setC == setTwo) and (not setC == setFive):
            stringThree = stringThree.join(setC)
        codeDict[3] = SortDigit(stringThree)


    def FindBottomLeft():
        setEight = set(codeDict[8])
        setThree = set(codeDict[3])
        setUpperLeft = set(upperLeft)
        setTemp = setEight - setThree
        setTemp = setTemp - setUpperLeft
        global bottomLeft
        for d in setTemp:
            bottomLeft = d


    def FindNine():
        setEight = set(codeDict[8])
        setBottomLeft = set(bottomLeft)
        setNine = setEight - setBottomLeft
        stringNine = ""
        stringNine = stringNine.join(setNine)
        codeDict[9] = SortDigit(stringNine)
        

    FindTopLine(codeDict)
    FindCenterLine(TwoThreeFive)
    FindZero()
    FindFive(TwoThreeFive)
    FindBottomRight()
    FindTwo(TwoThreeFive)
    FindUpperRight()
    FindSix()
    FindThree(TwoThreeFive)
    FindBottomLeft()
    # print("topLine:", topLine, "upperLeft:", upperLeft, "bottomLeft:", bottomLeft, "center:", centerLine, "bottomRight:", bottomRight, "upperRight:", upperRight)
    FindNine()



    # FIND SUM OF OUTPUT COLUMN NOW

    outputNum = ""

    for digit in outputList[testCase]:
        setA = set(digit)
        for i in codeDict:
            setB = set(codeDict[i])
            if setA == setB:
                outputNum = outputNum + str(i)

    outputNums.append(int(outputNum))
            
# print(outputNums)
print(sum(outputNums))

