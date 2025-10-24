def get_fahrenheit_from_celsius(numbers):
	return numbers * 1.8 + 32


numbers = [0, 20, 37, 100]
output = list(map(get_fahrenheit_from_celsius , numbers)) 

print(output)