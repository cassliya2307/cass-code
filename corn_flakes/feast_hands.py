def get_third_element(num):
	count = 0
	for numbers in range(len(num)):
		count += 1
		if numbers == 1:
			break
	
	return num[count]




def get_last_colour(colour):	
	colour.pop()
	colour.append("yellow")
	colour.append("purple")
	return colour

def remove_third_element(number):
	number.remove(3)


	return number

def return_list(words):
	count = 0
	number = []
	for letters in range(len(words)):
		count += 1		
		












def ascending_order(numbers):
	numbers.sort()
	
	return numbers

def new_list(numbers):
	count = -1
	number = []
	for num in range(len(numbers)):
		count += 1
		if count == 11:
			break
		store = numbers[count]
		number.append(store)

	return number


def combine_lists(num1, num2):
	count = -1
	store = 0
	for num in range(len(num2)):
		count += 1
		store = num2[count]
		num1.append(store)
	return num1


def list_string_greater_than_three(word):
	count = -1
	words = []
	for letter in range(len(word)):
		count += 1
		if len(word[count]) > 3:
			words.append(word[count])
	return words








num = [10, 20, 30 , 40 , 50]
print("1." ,get_third_element(num))

color = ["red", "green", "blue"]
print("2." ,get_last_colour(color))

num = [1, 2, 3, 4, 5]
print("3." ,remove_third_element(num))

my_list = ["Alice" , "Bob" , "Charlie"]
print("4." ,return_list(my_list))

num = [10, 20, 30 , 40 , 50, 4, 1, 3, 9, 2, 1, 2, 3, 4, 5]
print("5." ,new_list(num))


num = [4, 1, 3, 9, 2]
print("6." ,ascending_order(num))

num = [10, 20, 30 , 40 , 50]
num2 = [1, 2, 3, 4, 5]
print("7." ,combine_lists(num, num2))

words = ["lamb" , "kit" , "yam" , "kings", "dogs", "man"]
print("8." ,list_string_greater_than_three(words))


