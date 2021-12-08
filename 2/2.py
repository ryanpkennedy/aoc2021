list = open("data.txt").read().splitlines()

depth = 0
horiz = 0
aim = 0

for move in list: 
    moveArr = move.split()
    size = int(moveArr[1])
    moveDir = moveArr[0]
    if moveDir == "forward": 
        horiz += size
    elif moveDir == "up":
        depth -= size
    elif moveDir == "down":
        depth += size

print("result: ", depth * horiz)