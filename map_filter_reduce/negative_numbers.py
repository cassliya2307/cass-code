def remove_negative_numbers(numbers):
	if numbers >-1:
		return numbers

	


number = [3, -5, 6, -9, 2, 9, -15, 7, 6, -90]
output = list(filter(remove_negative_numbers, number))

print(output)