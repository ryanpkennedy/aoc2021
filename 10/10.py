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

score = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137,
}


errors = []

def checkLine(line):
    stack = []
    for i in line:
        if i in openings:
            # print("adding", i, "to stack")
            stack.append(i)
        elif i in closings:
            match = stack.pop()
            # print("popping", match, "from stack")
            if match != matches[i]:
                return i
        # print("stack:", stack)
    if len(stack) > 0:
        return 0
    return 0

for line in list:
    result = checkLine(line)
    if result == 0:
        pass
    elif result != 0:
        errors.append(result)

# calculate score
sum = 0
for i in errors:
    sum+= score[i]


print(sum) 

