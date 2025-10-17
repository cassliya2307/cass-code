import unittest

import transaction_functions


class TestTransactionFunctions(unittest.TestCase):
	
	def test_for_the_existence_of_get_deposit(self):
	
		transaction_functions.get_deposit(2500,200,[1,2])

	def test_for_the_existence_of_get_withdrawal(self):
		
		transaction_functions.get_deposit(2500,200,[1,2])

	def test_for_the_existence_of_get_transaction(self):
	
		transaction_functions.get_transaction([1,2])
