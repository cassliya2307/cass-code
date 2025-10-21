from multi_fuel_dispencer_function import*

receipts = []
main = """
~~~~~Welcome To Liya's Fuel Station~~~~~

1. Buy Petroleum
2. Show Transaction History

"""
while True:
	print(main)
	

	main_input = int(input("Enter operation: "))

	match main_input:
		case 1:
			available_petrol = """
Available petroleum
1. Petrol  ⇒  650/Liter
2. Diesel  ⇒  720/Liter
3. Kerosene ⇒ 550/Liter
4. Gas ⇒ 480/Liter

		"""	

			print(available_petrol)
			available_petrol_input = int(input("Enter operation: "))
			liter_or_amount = input("Liter or Amount: ").lower()			

			

			match available_petrol_input:
				case 1:
					match liter_or_amount:
						case "liter":
							petrol_in_liters = int(input("How much petrol are you buying(650/L): "))
							print(get_fuel_by_liters(available_petrol_input, petrol_in_liters, receipts))

						case "amount":
							petrol_in_amount = int(input("How much petrol are you buying(650/L): "))
							print(get_fuel_by_amount(available_petrol_input,petrol_in_amount, receipts)) 
						
						case _:

							print("invalid input!!")
							liter_or_amount = input("Liter or Amount: ").lower()


				case 2:
					match liter_or_amount:
						case "liter":
							diesel_in_liters = int(input("How much diesel are you buying(720/L): "))
							print(get_fuel_by_liters(available_petrol_input, diesel_in_liters, receipts))

						case "amount":
							diesel_in_amount = int(input("How much diesel are you buying(720/L): "))
							print(get_fuel_by_amount(available_petrol_input, diesel_in_amount, receipts))

						case _:

							print("invalid input!!")
							liter_or_amount = input("Liter or Amount: ").lower()
					

				case 3:
					match liter_or_amount:
						case "liter":
							kerosene_in_liters = int(input("How much kerosene are you buying(550/L): "))
							print(get_fuel_by_liters(available_petrol_input, kerosene_in_liters, receipts))


						case "amount":
							kerosene_in_amount = int(input("How much kerosene are you buying(720/L): "))
							print(get_fuel_by_amount(available_petrol_input, kerosene_in_amount, receipts))

						case _:

							print("invalid input!!")
							liter_or_amount = input("Liter or Amount: ").lower()
						


				
				case 4:
					match liter_or_amount:
						case "liter":
							gas_in_liters = int(input("How much gas are you buying(480/L): "))
							print(get_fuel_by_liters(available_petrol_input, gas_in_liters, receipts))



						case "amount":
							gas_in_amount = int(input("How much kerosene are you buying(720/L): "))
							print(get_fuel_by_amount(available_petrol_input, gas_in_amount, receipts))


						case _:

							print("invalid input!!")
							liter_or_amount = input("Liter or Amount: ").lower()
				case _:

					print("invalid number input, enter number in range 1-4")

		case 2:
			print(get_show_transcations(receipts))				

		



		case _: 
			print("invalid number input, enter number in range 1-2")		