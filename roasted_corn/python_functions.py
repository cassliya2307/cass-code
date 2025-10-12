def getlongestWord(string):
	largest = " "
	max = 0
	for words in (string):
		
		if len(words) > max:
			largest = words
			max = len(words)
						
	print(max)		
	return largest
				

def removeOddStrings(string):
	letter = " " 
	for word in (string):
		if len(word) % 2 != 0:
			letter = string.pop()
	
	

	return letter

def getlengthsmallest(num):
	length = 0
	for digits in (num):
		length += 1

		smallest = 0
		smallest = num[0]  
		for integer in range(1, length):
			if num[integer] < smallest:
				smallest = num[integer]

	return smallest

 
def getlength_largest(num):
	length = 0
	for digits in (num):
		length += 1

		largest = 0
		largest = num[0]  
		for integer in range(1, length):
			if num[integer] > largest:
				largest = num[integer]

	return largest


def multipleStrings(string, num):
	for digit in range(num - 1):
		print(string, end = " ")
	

	
	return string

def getlistSquared(num):
	num2 = []
	
	for digits in (num):
		num2.append(num * num)

	return num2
	
def getlistSquaredSum(num):
	num2 = []
	
	for digits in (num):
		num2.append(num * num)
		num2 += num2
	return num2


 

number = [67,35,5,-5,9,1]			

print(getlengthlargest(number))
print(getlistSquared(number))
