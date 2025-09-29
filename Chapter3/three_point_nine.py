number = int(input("Enter a five digit number: "))

divide = 10000

for number in range(5):
	digit = number // divide
	print(digit, end=" ")
	number = number % divide
	divide = divide // 10