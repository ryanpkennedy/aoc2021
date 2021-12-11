list = open("data.txt").read().split(",")

list = [int(a) for a in list]

fuelUsed = []

minPoint = 0
minFuel = max(list)*len(list)*len(list)
print("minfuel start: ", minFuel)

for point in range(max(list)):
    fuelUsed = []
    for x in list:
        distance = abs(x - point)
        fuel = int((1+distance)*distance/2)
        fuelUsed.append(fuel)
    totalFuel = sum(fuelUsed)
    if totalFuel < minFuel:
        minFuel = totalFuel
        minPoint = point
    
print(minPoint)
print(minFuel)

