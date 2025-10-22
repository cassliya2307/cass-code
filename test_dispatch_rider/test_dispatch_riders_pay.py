import unittest

import dispatch_riders_pay_function 

class TestForDispatchRidersPay(unittest.TestCase):

	def test_if_the_percentage_of_delivery_is_given_the_corresponding_pay(self):
		actual_1 = dispatch_riders_pay_function.get_dispatch_riders_pay(49)
	
		expected_1 = (160 * 49) + 5000

		self.assertEqual(actual_1 , expected_1)

		actual_2 = dispatch_riders_pay_function.get_dispatch_riders_pay(59)
	
		expected_2 = (200 * 59) + 5000

		self.assertEqual(actual_2 , expected_2)

		actual_3 = dispatch_riders_pay_function.get_dispatch_riders_pay(69)
	
		expected_3 = (250 * 69) + 5000

		self.assertEqual(actual_3 , expected_3)

		actual_4 = dispatch_riders_pay_function.get_dispatch_riders_pay(70)
	
		expected_4 = (500 * 70) + 5000

	

	def test_for_wrong_user_input(self):

		wrong_input_1 =	"123"
		self.assertRaises(TypeError, wrong_input_1)
		
		wrong_input_2 =	70.8
		self.assertRaises(TypeError, wrong_input_2)
		



	def test_for_wrong_rate_input(self):
		self.assertRaises(ValueError,dispatch_riders_pay_function.get_dispatch_riders_pay, 101)



	def test_for_negative_number(self):
		self.assertRaises(ValueError,dispatch_riders_pay_function.get_dispatch_riders_pay, -1)
