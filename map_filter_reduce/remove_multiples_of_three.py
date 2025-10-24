def remove_numbers_divisible_by_three(numbers):
	if numbers % 3 != 0:
		return numbers

	


number = [3, 5, 6, 9, 2, 1, 9, 15, 7, 6, 90]
output = list(filter(remove_numbers_divisible_by_three, number))

print(output)