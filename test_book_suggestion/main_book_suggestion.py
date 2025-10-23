from book_suggestion_functions import*

my_book_list = ["my happy life", "dork diaries", "spyxfamily", "demon slayer", "naruto", "boruto", "solo leveling" ,"attack on titan" , "my hero academia", "dan da dan" , "blue lock", "one piece" , "jujutsu kaisen", "apothecary diaries", "darling in a franxx", "i want to eat your pancreas", "mob psycho 100", "kuroku no basket", "call of the night"]


details = """
Welcome to the Book Suggestion System!

1. Get Suggestions
2. Add Book
3. Remove Book
4. Update Book
5. Show All Books 

"""
while True:
	print(details)

	detail_input = input("Enter a number from the menu: ")

	match detail_input:
		case "1":
			while True:
				print("The book is:" , end = " ")
				book, page = suggest_book(my_book_list)
				print(book, "Pages:",page)
				book = input("Do you want me to keep suggesting(yes/no): ").lower()
			
				if book != "yes":
					break
	
	

		case "2":
			add_a_book = input("Add a book: ").lower()
			add_book(add_a_book , my_book_list)
			print("You've successfully added a book!")
			#print(add_book(add_a_book, my_book_list))



		case "3":
			remove_a_book = input("Enter the name of the book to remove: ").lower()
			remove_book(remove_a_book , my_book_list)
			print("Book removed successfully!")
			#print(remove_book(remove_a_book , my_book_list))
	


		case "4":
			update_a_book = input("Enter the old title: ").lower()
			add_new_book = input("Enter the new title: ").lower()
			print(update_book(update_a_book, add_new_book, my_book_list))

	
		case "5":
			print(show_all_books(my_book_list))
