def get_even_numbers(numbers):
	if numbers % 2 == 0:
		return numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = list(filter(get_even_numbers , numbers))

print(output)