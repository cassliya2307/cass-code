def getStringLength(name):
	length_number = 0;
	for letters in name:
  		length_number = length_number + 1;

	return length_number


def getReverse(word):
	reverse = " "
	for letters in word:
		reverse = letters + reverse

	return reverse

			
		



def getTime(minutes):
	hour = minutes / 60
	seconds = minutes * 60

	print(hour)
	return seconds;


def getVowels(fruit):
	vowel = 0;

	for letters in fruit:
		if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u':
			vowel += 1
			
		
	return vowel
		
def getSmallest(number):
	smallest = 0;
	smallest = num[0]  
	for integer in range(1, len(num)):
		if num[integer] < smallest:
			smallest = num[integer]

	return smallest

def getAverage(num):
	average = 0
	sum = 0
	for count in range(len(num)):
		sum += 1
	average = sum / count
	
	return average		
	

def occurence(num1 , num2):
	target = num2
	sum = 0
	for count in range(len(num)):
		if num1[count] == num2:
			sum+=1
	return sum


def firstNumber(num):
	first = num[0]
	return first


def getlastNumber(num):
	last = 0
	for count in range(len(num)):
		last = num[count - 1]
	return last


def getLength(num):
	length = 0
	for count in range(len(num)):
		length += 1
	return length

def getmiddleNumber(num):
	middle = 0
	for count in range(len(num)):
		middle = num[(len(num) - 1) // 2] 
		
	return middle

def getTruth(num1 , num2):
	target = num2
	contain = True
	for count in range(len(num)):
		if num2 == num[count]:
			contain = True
		else: contain = False
	return contain



def getlastAndFirst(num):
	first = num[0]
	last = 0
	temp = 0
	for count in range(len(num)):
		last = num[count - 1]
		temp = num[0]
		first = last
		last = temp

	print(first)
	return last









print(getStringLength("characters"))

print(getVowels("pineapple"))

print(getReverse("character"))

num = [9,2,6,5,5]
print(getSmallest(num))	

print(getAverage(num))

print(getTruth(num , 5))






