def only_floats(num1 , num2):
	
	decimal_num1 = num1 + 0.00
	decimal_num2 = num2 + 0.00

	if num1 == decimal_num1 and num2 == decimal_num2:
		return 2
	
	elif num1 == decimal_num1 or num2 == decimal_num2:
		return 1

	else: 
		return 0


num1 = input("Enter first number: ")
num2 = input("Enter first number: ")

print(only_floats(num1 , num2))