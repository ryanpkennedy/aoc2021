list = open("data.txt").read()

list = list.split("\n\n")

bingoNums = [17,2,33,86,38,41,4,34,91,61,11,81,3,59,29,71,26,44,54,89,46,9,85,62,23,76,45,24,78,14,58,48,57,40,21,49,7,99,8,56,50,19,53,55,10,94,75,68,6,83,84,88,52,80,73,74,79,36,70,28,37,0,42,98,96,92,27,90,47,20,5,77,69,93,31,30,95,25,63,65,51,72,60,16,12,64,18,13,1,35,15,66,67,43,22,87,97,32,39,82
]
totalBoards = len(list)

for x in range(len(list)): 
    list[x] = list[x].splitlines()
    list[x] = [row.split() for row in list[x]]
    list[x] = list[x] + [[5,5,5,5,5]] + [[5,5,5,5,5]]

rowCount = len(list[0]) - 2
columnCount = len(list[0][0])

lastCalled = '0'

def updateBoard(board, num):
    # print("row status : ", board[5], "column status: ", board[6])
    # print("num being checked: ", num)
    for n in range(rowCount):
        for m in range(columnCount):
            global lastCalled
            lastCalled = board[n][m]
            if board[n][m] == num:
                board[n][m] = 'x'
                board[5][n] -= 1
                board[6][m] -= 1
                # print("updated board at row ", n, " and column ", m, board)
                return board
    return board


def checkBoard(board):
    for n in range(rowCount):
        for m in range(columnCount):
                if board[5][n] == 0 or board[6][m] == 0:
                    return True
    return False

def findWinner():
    for num in bingoNums:
        # for board in list:
        for x in range(len(list)):
            if list[x] == None:
                continue
            list[x] = updateBoard(list[x], str(num))
            check = checkBoard(list[x])
            if check == True:
                global totalBoards
                if totalBoards == 1: 
                    return list[x]
                list[x] = None
                totalBoards -= 1
    return None

sum = 0

winningBoard = findWinner()

if winningBoard != None: 
    for n in range(rowCount):
            for m in range(columnCount):
                if winningBoard[n][m] != 'x': 
                    sum += int(winningBoard[n][m])

    print(winningBoard)
    print('last called: ', lastCalled)
    print('result sum: ', sum)
    print('result: ', sum * int(lastCalled))

