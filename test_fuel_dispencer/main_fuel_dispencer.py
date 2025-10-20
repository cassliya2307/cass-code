from multi_fuel_dispencer_function import*

main = """
~~~~~Welcome To Liya's Fuel Station~~~~~

1. Buy Petroleum
2. Show Transaction History

"""

print(main)

main_input = int(input("Enter operation: "))

match main_input:
	case 1:
		available_petrol = """
Available petroleum
 1. Petrol  ⇒  650 / Liter
 2. Diesel  ⇒  720 /Liter
 3. Kerosene ⇒  550 /Liter
 4. Gas  ⇒   480 /Liter

		"""
		print(available_petrol)
		available_petrol_input = int(input("Enter operation: "))
		liter_or_amount = input("Liter or Amount: ").lower()

		match available_petrol_input:
			case 1:
				if liter_or_amount == "liters" or "liter":
					petrol_in_liters = int(input("How much petrol are you buying(650/L): "))
					print(get_fuel_by_liters(available_petrol_input, petrol_in_liters))
				