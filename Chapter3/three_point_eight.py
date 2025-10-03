total = 0
product = 1
smallest = 0
largest = 0


for num in range(1, 5):
	num = int(input("Enter number: "))

	total += num
	product *= num 

	if smallest == 0 or num < smallest:
		smallest = num

	if largest == 0 or num > largest:
		largest = num


average = total / 4

print("The total is" ,total)

print("The product is" ,product)

print("The smallest is" ,smallest)

print("The largest is" ,largest)

print("The average is" ,average)

