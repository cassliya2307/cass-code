def get_deposit(account_balance, amount,  transactions = []):
	account_balance += amount
		
	
	return account_balance


def get_withdrawal(account_balance, amount,  transactions = []):
	if amount > account_balance:
		account_balance = account_balance - 0
		print("Transaction failed, Insufficient balance")
	else:
		account_balance -= amount
			
	return account_balance


def get_transaction(transactions = []):
	...