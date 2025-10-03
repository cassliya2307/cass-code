def divide_or_square(num):
	if num % 5 == 0:
		return num**0.5
	else:
		return num % 5

num = int(input("Enter a number: "))