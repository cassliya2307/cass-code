from functools import reduce

def get_the_product(numbers, number):
	return numbers * number



numbers = [21 , 10 , 10]
output = reduce(get_the_product, numbers)

print(output)