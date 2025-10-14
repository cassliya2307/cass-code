number = [1,7,8,9]
count = 1
sum = 0
for num in range(len(number)):
	if count % 3 == 0: 
		sum *= number[count]
	
	count += 1
	
print(sum)