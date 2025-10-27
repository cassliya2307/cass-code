import unittest
from unmodified_tuple import*
class TestToAddNumberToATupleWithoutModfyingIt(unittest.TestCase):

	def test_if_there_are_numbers_in_the_tuple_is_the_same_with_the_returned_value(self):
		actual = unmodified_tuple(9, 1, [9],3 ,4)
		
		expected = 9, 1, [9, 5] ,3 ,4

		self.assertEqual(actual, expected)


	
	def test_if_the_returned_value_has_a_list_with_two_elements(self):
		actual = modified_list(9, 1, [9, 9],3 ,4)
		
		expected = 9, 1, [9, 99] ,3 ,4

		self.assertEqual(actual, expected)

		
	def test_if_the_value_is_a_list(self):
		actual = convert_tuple_to_list("apple" , "banana" )
		expected = ["apple" , "banana" , "mango"]
		self.assertEqual(actual, expected)

	
	def test_for_the_return_type_of_the_twoD_list(self):
		actual = add_inner_list([[2, 3, 4], [1,5,7] , [4,6,8]]
)
		expected = [9, 13, 18]
		self.assertEqual(actual, expected)




	def test_for_the_return_type_of_the_second_twoD_list(self):
		actual = add_inner_elements_with_the_same_indexes([ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]
)
		expected =  [7, 14, 19]
		self.assertEqual(actual, expected)

	def test_for_accurate_return_value(self):
		actual = filter_even_numbers(4)
	
		expected = 4
		
		self.assertEqual(actual, expected)



	#def test_that_it_returns_strings_with_only_three_characters(self):
		#actual = get_string_less_than_four(["naomi" , "cat" , "salmon", "rat"])
		#expected = ["cat" , "rat"]
		#self.assertEqual(actual, expected)

	
	#def test_that_it_returns_tuple_first_value_greater_than_2(self):
		#actual = get_grades_in_tuple([(1, "A") , (2 , "B") , (3 , "C") , (4, "D")])
		#expected = [(2 , "B") , (3 , "C") , (4, "D")]
		#self.assertEqual(actual, expected)

	


	def test_for_accurate_return_value_two(self):
		actual = filter_multiple_of_three_and_five(15)
	
		expected = 15
		
		self.assertEqual(actual, expected)



	#def test_for_return_value(self):
		#actual = get_pallindrum(["level" , "madam" , "love"])
		#expected = ["level" , "madam"]
		#self.assertEqual(actual, expected)


	#def test_if_the_return_type_is_uppercase(self):
		#actual = to_uppercase(["code"])
		#expected = CODE
		#self.assertEqual(actual, expected)

