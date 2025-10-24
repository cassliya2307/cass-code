def remove_none_values(values):
	if values != None:
		return values


values = [1, None, 7, None, 9, None, 9, 0, None, 9]
output = list(filter(remove_none_values, values))

print(output)