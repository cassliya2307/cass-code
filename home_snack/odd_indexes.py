number = [3,4,5,6,7,8]
count = 0
sum = 0
for num in range(len(number)):
	if count % 2 != 0:
		sum += number[num]
	
	count += 1

print(sum)