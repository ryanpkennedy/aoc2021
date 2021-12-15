list = open('data.txt').read().split()

for x in range(len(list)):
    list[x] = [i for i in list[x]]

minArray = []

for n in range(len(list)):
    for m in range(len(list[0])):
        current = int(list[n][m])
        top = 9
        bottom = 9
        left = 9
        right = 9
        if n > 0:
            top = int(list[n-1][m])
        if n < (len(list) -1):
            bottom = int(list[n+1][m])
        if m > 0:
            left = int(list[n][m-1])
        if m < (len(list[0])-1):
            right = int(list[n][m+1])
        if current < left and current < right and current < top and current < bottom:
            minArray.append(current)

# print(minArray)
danger = [x + 1 for x in minArray]
# print(danger)
print(sum(danger))