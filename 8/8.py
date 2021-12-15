list = open('data.txt').read().splitlines()


for x in range(len(list)):
    list[x] = list[x].split(" | ")
    list[x] = list[x][1]
    list[x] = list[x].split(" ")

print(list)

count = 0

for line in list:
    for digit in line:
        length = len(digit)
        if length == 2 or length == 3 or length == 4 or length == 7:
            count+=1

print(count)
