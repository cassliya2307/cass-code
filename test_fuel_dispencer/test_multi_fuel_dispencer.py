import unittest

from multi_fuel_dispencer_function import*


class TestForMultiFuelDispencer(unittest.TestCase):

	def test_for_the_existence_of_get_fuel_by_liters(self):

		get_fuel_by_liters(67 , 2)
		
	def test_for_negative_number_in_liters(self):
		actual = get_fuel_by_liters(1, -12)
		expected = 0
		self.assertEqual(actual, expected)

	def test_for_the_existence_of_get_fuel_by_amount(self):

		get_fuel_by_amount(67 , 2500)

	def test_for_negative_number_in_amount(self):
		actual = get_fuel_by_liters(1, -12)
		expected = 0
		self.assertEqual(actual, expected)

	