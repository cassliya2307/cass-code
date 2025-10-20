import unittest

import  multi_fuel_dispencer_function


class TestForMultiFuelDispencer(unittest.TestCase):

	def test_for_the_existence_of_get_fuel_by_liters(self):

		multi_fuel_dispencer_function.get_fuel_by_liters(67)

	def test_for_the_existence_of_get_fuel_by_amount(self):

		multi_fuel_dispencer_function.get_fuel_by_amount(67)