num = [2,3,-5,8,1]
smallest = 0;
smallest = num[0]  
for integer in range(1, len(num)):
	if num[integer] < smallest:
		smallest = num[integer]


print(smallest)