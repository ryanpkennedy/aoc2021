list = open("data.txt").read().split(",")

list = [int(a) for a in list]

days = 256

dayTracker = [0 for x in range(9)]

for fish in list: 
    dayTracker[fish] += 1

for day in range(days):
    newFish = dayTracker[0]
    for x in range(len(dayTracker)):
        dayTracker[x] =  (x < 8 and dayTracker[x + 1]) + ((x == 8 or x == 6) and newFish)

print(sum(dayTracker))