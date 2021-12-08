list = open("test.txt").read().splitlines()

depth = 0
horiz = 0
aim = 0

for move in list: 
    moveArr = move.split()
    size = int(moveArr[1])
    moveDir = moveArr[0]
    if moveDir == "forward": 
        horiz += size
        depth += size * aim
    elif moveDir == "up":
        aim -= size
    elif moveDir == "down":
        aim += size
    print("depth: ", depth, "\n", "horiz: ", horiz)

print("result: ", depth * horiz)