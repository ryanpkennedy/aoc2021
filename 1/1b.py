list = open("data.txt").read().splitlines()

list = [int(num) for num in list]

count = 0
sum1 = 0
sum2 = 0


for x in range(len(list)-3):
	sum1 = list[x] + list[x+1] + list[x+2]
	sum2 = list[x+1] + list[x+2] + list[x+3]
	if sum2 > sum1: 
		count += 1
	
print(count)