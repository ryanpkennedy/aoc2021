list = open("data.txt").read().splitlines()

# print(list)

count = 0
case = 0

print(len(list))

for x in range(len(list)-1):
	if int(list[x+1]) > int(list[x]):
		count += 1
	
print(count)