from functools import reduce

def unmodified_tuple(*number):
	number[2].append(5)
	return number
	


def modified_list(*number):
	number[2].pop()
	number[2].append(99)
	return number

def convert_tuple_to_list(*fruits):
	result = []
	result2 = []
	result = list(fruits)
	result2 = result.append("mango")
	return result

def unpack_tuple(*numbers):
	number1 = numbers[0]
	number2 = numbers[1]
	others	= numbers[2: : 1]
	print(number1 , end = " ")
	print(number2 , end = " ")
	print(others , end = " ")
	return ""

def add_inner_list(numbers):
	all_numbers = []
	count = 0
	count2 = 0
	count3 = 0
	digit = 0
	digit2 = 0
	digit3 = 0
	for num in numbers:
		digit += numbers[0][count]
		count += 1
	all_numbers.append(digit) 
	for num in numbers:
		digit2 += numbers[1][count2]
		count2 += 1
	all_numbers.append(digit2) 
	
	for num in numbers:
		digit3 += numbers[2][count3]
		count3 += 1
	all_numbers.append(digit3) 
	
	return all_numbers

def add_inner_elements_with_the_same_indexes(numbers):
	new_list = []
	count = 0
	digit = 0
	digit1 = 0
	digit2 = 0
	for num in numbers:
		digit += num[count]
		digit1 += num[count + 1]
		digit2 += num[count + 2]
		
	new_list.append(digit)
	new_list.append(digit1)
	new_list.append(digit2)
	return new_list	

def filter_even_numbers(number):
	if number % 2 == 0 and number <= 21 and number >= 1:
		return number	

def get_string_less_than_four(strings):
	count = 0
	for words in range(len(strings)):
		count += 1
		if strings[count] <= 3:
			return strings	


#def get_grades_in_tuple(number_grade):
	#count = -1
	#for num in number_grade:
		#count += 1
		#print(number_grade[count])
		#if number_grade[count] == int and number_grade[count] >= 2:
			#return number_grade[num]


def filter_multiple_of_three_and_five(number):
	if number % 3 == 0 and number % 5 == 0 and number <= 51 and number >= 1:
		return number	



#def get_pallindrum(words):
	#reverse = 
	#for word in words:
		


def to_uppercase(words):
	count = -1
	new_list = []
	for word in words:
		count += 1
		return words.upper()
		

def square(number):
	if number >= 1 and number <= 10:
		return number ** 2


def add_ten_percent_plus_price(price):
	return price + price * 10//100


def get_the_sum_of_numbers(number , store):
		my_list =  list(range(1,51))
			return my_list + store
	
def get_largest_number(number, largest):
		if number > largest:
			return largest = number

def concatinate_string(words , letter):
	return words + " " + letter


def get_squares(number):
	return number ** 2

def get_product(get_squares, num):
	return number * num
	

number = 6, 8, [8], 9, 0
#print("1." ,unmodified_tuple(*number))

num = 1, 2, [3,4], 5
#print("2." ,modified_list(*number))

fruits = "apple" , "pineapple", "banana", "orange"
#print("3." ,convert_tuple_to_list(*fruits))

numbers = 10, 20, 30,40
#print(unpack_tuple(*numbers))


numbers = [[2, 3, 4], [1,5,7] , [4,6,8]]
#print(add_inner_list(numbers))


print(add_inner_elements_with_the_same_indexes(numbers))

number = [1, 45, 6, 8, 9,2, 3,5,68 ,8,20,3,5,78,3,57,2,6,20,18]
output = list(filter(filter_even_numbers, number))
print(output)

words = ["puppy" , "kitty" , "turtle"]
output = list(filter(to_uppercase, words))
print(output)

number = [1 ,3 , 4, 5, 5,7 ,8,10]

output = list(map(square , number))

print(output)

prices = [100, 200, 300]
result = list(map(add_ten_percent_to_price,prices))

print(result)

result = reduce(get_the_sum_of_numbers, number)
print(result)

result = reduce(get_largest_number, number)
print(result)


words = ["I" , "Love", "Anime"]
output = reduce(concatinate_string , words)

print(output)


result = list(map(get_squares , number))
print(result)


output = reduce(get_product,result)
print(output)
