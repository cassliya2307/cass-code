num = [3,12,7,21,8]
count = 0
num2 = []

smallest = num[0]  
for integer in range(len(num)):
	if num[count] < smallest:
		smallest = num[count]	

for numbers in range(len(num)):
	if num[count] < num[-1]:
		num2 = num[count]
		count += 1
	
			
	if num[count] > smallest and num[count] < num[-1]:
		num2 = num[count]
		count += 1
		

	print(num[count])	
		
#num2 = [min, min2 , min3 , min4 , min5]	
	
	#print(num[count])
print(num2)
	#print(min)


