import unittest

import book_suggestion_functions

class TestForBookSuggestions(unittest.TestCase):

	def test_for_the_existence_of_suggest_book(self):
		
		book_suggestion_functions.suggest_book(["book", "books"])

	

	def test_for_the_existence_of_add_book(self):
		
		book_suggestion_functions.add_book(["book" , "books"] , "naomi")
	
	
	def test_for_the_existence_of_remove_book(self):

		book_suggestion_functions.remove_book(["book" , "books"] , "naomi")

	
	def test_for_the_existence_of_update_book(self):

		book_suggestion_functions.update_book("page" , "book" , ["book" , "books"])


	def test_for_the_existence_of_show_all_books(self):
		
		book_suggestion_functions.show_all_books(["book" , "books"])




		
