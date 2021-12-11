list = open("data.txt").read().split(",")

list = [int(a) for a in list]

days = 256

dayTracker = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0, 
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for fish in list: 
    dayTracker[fish] += 1

def CountFish(): 
    finalCount = 0
    for day in dayTracker:
        finalCount += dayTracker[day]
    return finalCount

for day in range(days):
        newFish = dayTracker[0]
        dayTracker[0] = dayTracker[1]
        dayTracker[1] = dayTracker[2]
        dayTracker[2] = dayTracker[3]
        dayTracker[3] = dayTracker[4]
        dayTracker[4] = dayTracker[5]
        dayTracker[5] = dayTracker[6]
        dayTracker[6] = dayTracker[7] + newFish
        dayTracker[7] = dayTracker[8]
        dayTracker[8] = newFish

print(CountFish())