list = open("data.txt").read()

list = list.split("\n\n")
testList = list[2]

# testNums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
bingoNums = [17,2,33,86,38,41,4,34,91,61,11,81,3,59,29,71,26,44,54,89,46,9,85,62,23,76,45,24,78,14,58,48,57,40,21,49,7,99,8,56,50,19,53,55,10,94,75,68,6,83,84,88,52,80,73,74,79,36,70,28,37,0,42,98,96,92,27,90,47,20,5,77,69,93,31,30,95,25,63,65,51,72,60,16,12,64,18,13,1,35,15,66,67,43,22,87,97,32,39,82
]


# Board = list[2].splitlines()

# Board = [row.split() for row in Board]

for x in range(len(list)): 
    list[x] = list[x].splitlines()
    list[x] = [row.split() for row in list[x]]
    list[x] = list[x] + [[5,5,5,5,5]] + [[5,5,5,5,5]]
    print(list[x])

rowCount = len(list[0]) - 2
columnCount = len(list[0][0])

lastCalled = '0'

def updateBoard(board, num):
    print("row status : ", board[5], "column status: ", board[6])
    print("num being checked: ", num)
    for n in range(rowCount):
        for m in range(columnCount):
            global lastCalled
            lastCalled = board[n][m]
            if board[n][m] == num:
                board[n][m] = 'x'
                board[5][n] -= 1
                board[6][m] -= 1
                print("updated board at row ", n, " and column ", m, board)
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
        for board in list:
            board = updateBoard(board, str(num))
            check = checkBoard(board)
            if check == True:
                print("bingo!")
                return board
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

