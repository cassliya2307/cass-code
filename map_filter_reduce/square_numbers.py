def square_numbers(numbers):
	return numbers ** 2

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
output = list(map(square_numbers, num))

print(output)