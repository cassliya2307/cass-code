def get_fuel_by_liters(number, liter, receipt = []):
	if number == 1 and liter > 0 and liter <= 50:
		amount = liter *  650
		receipt_paper = f"""
		================================
		= Product: Petrol	       =
		= Amount: N{amount:<8}	       =
		= Liters: {liter}L  	       = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper


	elif number == 2 and liter > 0 and liter <= 50:
		amount = liter * 720
		receipt_paper = f"""
		================================
		= Product: Diesel	       =
		= Amount:N{amount:<8}	       =
		= Liters: {liter}L    	       = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper


	elif number == 3 and liter > 0 and liter <= 50:
		amount = liter * 550
		receipt_paper = f"""
		================================
		= Product: Kerosene	       =
		= Amount: N{amount:<8}	       =
		= Liters: {liter}L     	       = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper

	
	elif number == 4 and liter > 0 and liter <= 50:
		amount = liter * 480
		receipt_paper = f"""
		================================
		= Product: Gas  	       =
		= Amount: N{amount:<8}	       =
		= Liters: {liter}L    	       = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper


	else: print("Liters must be between 1 - 50!!!")
	return 0
		
		

def get_fuel_by_amount(number, amount, receipt = []):
	if number == 1 and amount >= 650:
		liter = amount / 650
		receipt_paper = f"""
		================================
		= Product: Petrol	       =
		= Amount: N{amount:<8} 	       =
		= Liters: {liter:.2f}L         = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper

	elif number == 2 and amount >= 720:
		liter = amount / 720
		receipt_paper = f"""
		================================
		= Product: Diesel	       =
		= Amount:N{amount:<8} 	       =
		= Liters: {liter:.2f}L         = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper

	elif number == 3 and amount >= 550:
		liter = amount / 550
		receipt_paper = f"""
		================================
		= Product: Kerosene	       =
		= Amount: N{amount:<8} 	       =
		= Liters: {liter:.2f}L 	       = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper

	elif number == 4 and amount >= 480:
		liter = amount / 480
		receipt_paper = f"""
		================================
		= Product: Gas		       =
		= Amount: N{amount:<8} 	       =
		= Liters: {liter:.2f}L         = 
		= Thank you for your patronage =
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""
		receipt.append(receipt_paper)
		return receipt_paper
	else: print("Amount must be above a liter price!!!")
	return 0


def get_show_transcations(receipt = []):
	if receipt == []:
		print("	No transactions made!")
	else:
		for index in receipt:
			print(index)
	
	return " "
	


