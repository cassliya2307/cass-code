import random
from random import randint
def suggest_book(books):
	choice = random.choice(books)
	pages = randint(1, 100)
	return choice , pages


def add_book(book , books):
	books.append(book)
	return books

def remove_book(book , books):
	for index in books:
		if book == index:
			books.remove(index)	


	return books
	

def update_book(book, page, books):
	for index in books:
		
		if book == index:
			books.remove(index)

	books.append(page)

	return books

def show_all_books(books):
	list = " "
	for index in books:
		print(index)		
	return " "
	