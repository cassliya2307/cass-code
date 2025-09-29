num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
	max1 = num1
	max2 = num2
else:
	max1 = num2
	max2 = num1

for number in range(3, 11):
	num = int(input(f"Enter number {number}: "))
	if num > max1:
		max2 = max1
		max1 = num
	elif num > max2 and num != max1:
		max2 = num

print("The largest is: ",max1)
print("The second largest is: ",max2)