def get_deposit(account_balance, amount,  transactions):
	account_balance += amount
	transactions = f"Deposited: N{amount} | New Balance: N{account_balance}"
	
	return account_balance





def withdraw_money(account_balance,amount, transactions):
	if amount < account_balance:
		account_balance -= amount
		transactions = f"Withdrew: N{amount} | New Balance: N{account_balance}"
	else:
		account_balance = account_balance
		transactions = f"Withdrawal failed: insufficient funds"

	return account_balance





def show_transaction_history(amount, account_balance, transactions):
	transactions = []
	
	





transact = ""
balance = 0
exit = True
choice = 0

menu = """
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
			money = int(input("Enter deposit amount: "))
			balance = get_deposit(balance,money, transact)
			print("N",balance)
			
				
			
			
		
		case 2:
			money = int(input("Enter withdrawal amount: "))
			balance = withdraw_money(balance, money, transact)
			print("N", balance)
		

		case 3:
			
		case 4:
			print("Your final balance is: ",balance)
			print("Thank you for using our Transaction Log App")
			print("Feel free to come back anytime")		






















