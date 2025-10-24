def add_ten_to_each_element(number):
	return number + 10

integers = [2, 4, 6, 7, 9, 0]
output = list(map(add_ten_to_each_element, integers))
print(output)