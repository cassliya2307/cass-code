def get_dispatch_riders_pay(rate):
	if rate < 1:
		raise ValueError("Input rate from range 1-100")

	else:
		if type(rate) == int:
			if rate < 50:
				amount = 160 * rate + 5000
				return amount
			elif rate >= 50 and rate < 60:
				amount = 200 * rate + 5000
				return amount 
			elif rate >= 60 and rate < 70:
				amount = 250 * rate + 5000
				return amount 
			elif rate >= 70 and rate <= 100:
				amount = 500 * rate + 5000
				return amount 
		
			else:
				raise ValueError("Invalid pay")
		else:
			raise TypeError("Invalid Input, input should be a number")

	
	