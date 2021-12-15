import math

list = open('data.txt').read().splitlines()

testCase = 2

item = list[testCase]

openings = set(['[','{', '(', '<'])
closings = set([']','}', ')', '>'])

matches = {
    '>':'<',
    ')':'(',
    '}':'{',
    ']':'[',
}

closeMatches = {
    '<':'>',
    '(':')',
    '{':'}',
    '[':']',
}

score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


errors = []

def autoComplete(stack):
    newStack = []
    for x in range(len(stack)):
        nextOpening = stack.pop()
        nextClosing = closeMatches[nextOpening]
        newStack.append(nextClosing)
    return newStack



def calcScore(stack):
    sum = 0
    for i in stack:
        sum = sum*5 + score[i]
    return sum


def checkLine(line):
    stack = []
    for i in line:
        if i in openings:
            stack.append(i)
        elif i in closings:
            match = stack.pop()
            if match != matches[i]:
                return None
    if len(stack) > 0:
        newStack = autoComplete(stack)
        return newStack
    return None

scoresArray = []
for line in list:
    result = checkLine(line)
    if result == None:
        continue
    if len(result) > 0:
        sum = calcScore(result)
        scoresArray.append(sum)

scoresArray.sort()

print('length of scores array:', len(scoresArray))
middle = int(math.floor((len(scoresArray)/2)))
print('middle index:', middle)

result = scoresArray[middle]

print(result) 

