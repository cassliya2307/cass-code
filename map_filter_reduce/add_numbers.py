from functools import reduce

def get_the_sum(numbers, number):
	return numbers + number



numbers = [1,10, 10]
output = reduce(get_the_sum, numbers)

print(output)