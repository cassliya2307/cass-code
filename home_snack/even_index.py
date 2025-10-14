number = [2,4,5,6,7]
count = 0
sum = 0
for num in range(len(number)):
	if count % 2 == 0:
		sum += number[count]

	count += 1

print(sum)