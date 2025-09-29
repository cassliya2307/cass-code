pi = 0.0
print("Number\tApproximation")

for number in range(1, 5):
	pi = 0.0
	sign = 1
	denominator = 1
	for num in range(number):
		pi += sign * 4 / denominator
		denominator += 2
		sign = -sign
	print(f"{number}\t{pi}")