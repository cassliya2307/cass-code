def factorOf(int num):

sum = 0
	for num in range(1,num,1):
		if num % counter == 0:
			sum += 1


	return sum


def isPrime(int num):

prime = 0
	for(1,num,1):
		prime += counter

		if(prime % 2 != 0 || prime % num == 0):
		return true;

		else:return false

def isOdd(int number):
	return number%2!=0


def isLeapYear(int year):
boolean isLeap = false; 

	if(year % 4 == 0 && year % 100 != 0):
		isLeap = true



	else if(year % 4 == 0 && year % 100 == 0 && year % 400 == 0):
		isLeap = true

   

	else if(year % 4 == 0 && year % 100 == 0 && year % 400 != 0):
		isLeap = false



	if(isLeap == true):return true
	else:return false


def fahrenheitToCelsius(int num):
	celsius = 5 * (num - 32) / 9

	return celsius



def isEven(int number):
	return number % 2 = 0

def toSubtract(int num1 , int num2):
subtract = num1 - num2

	if(subtract < 1):
		return subtract *= -1

	else:return subtract


def toDivide(int num1 , int num2):
divide = num1 / num2

	if(num2 == 0 || num1 == 0):return divide = 0

	else:return divide

def isSquare(int num):
divide = num * 0.5
divide2 = divide *  divide
	if(divide2 == num):return true

	else:return false


def isSquare(int number):
factorial = 1
	for(1,number,1):
		factorial *= count

return factorial


def isPalindrum(int num):
digit = 0
reverse = 0
times = 10
check = num
	for(1,-1,1):
		digit = num % 10
		num = num / 10
		reverse *= times + digit

		if(count == 1):reverse = digit * 1


	if(check == reverse):return true

	else:return false