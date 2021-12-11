list = open("data.txt").read().split(",")

list = [int(a) for a in list]

# fuelUsed = []

minPoint = 0
minFuel = max(list)*len(list)

for point in list:
    fuelUsed = []
    for x in list:
        fuel = abs(x - point)
        fuelUsed.append(fuel)
    totalFuel = sum(fuelUsed)
    if totalFuel < minFuel:
        minFuel = totalFuel
        minPoint = point
    
print(minFuel)