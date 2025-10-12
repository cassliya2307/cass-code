def getlastTwoCharacters(string):
	string = "ataat"
	first = " "
	second = " "
	if len(string) < 2:
		result = " "
		print(result)	

	else:
		first = string[0] + string[1]
		second = string[-2] + string[-1]
		result = first + second

		print(result)
