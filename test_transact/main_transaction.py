from transaction_functions import*

transactions = []
balance = 0
exit = True
choice = 0

menu = """
~~~~~~MENU~~~~~~
1.Deposit money
2.Withdraw money
3.Show transaction
4.Exit the program
	
	"""
while choice != 4:
	print(menu)
	choice = int(input("Enter your choice: "))
	match choice:
		case 1:
			money = float(input("Enter deposit amount: "))
			balance = get_deposit(balance,money)
			print("N",balance)
			transactions.append(f"Deposited: N{money} | New Balance: N{balance}")
			
			
				
			
			
		
		case 2:
			money = float(input("Enter withdrawal amount: "))
			balance = get_withdrawal(balance, money)
			print("N",balance)
			transactions.append(f"Withdrew: N{money} | New Balance: N{balance}")
			


		case 3:
			if transactions == []:
				print("No transactions made")
			else:
				for index in range(len(transactions)):
					print(transactions[index])
			
				
		case 4:
			print("Your final balance is: ",balance)
			print("Thank you for using our Transaction Log App")
			print("Feel free to come back anytime")		



		case _:print("Invalid Input!!!")






