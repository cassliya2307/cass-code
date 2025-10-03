def future_investments(investment_amount, monthly, year):

	future_investments = investment_amount * (1 +  monthly)**year

	return future_investments


investment_amount = int(input("Enter investment amount: "))

monthly = int(input("Enter monthly interest: "))

year = int(input("Enter number of years: "))

print(future_investments(investment_amount, monthly, year))

	