list = open("data.txt").read().split(",")

list = [int(a) for a in list]

days = 80

for day in range(days): 
    # print("day ", day, "list: ", list)
    for x in range(len(list)): 
            if list[x] == 0:
                list[x] = 6
                list.append(8)
            else:
                list[x] -= 1


# print("day ", days, "list: ", list)
print(len(list))