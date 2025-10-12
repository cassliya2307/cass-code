def getverb(string):
	string = "string"

	if len(string) < 3:
		print(string)

	elif string[-3] == "i" and string[-2] == "n" and string[-1] == "g":
		string = string + "ly"

	else:
		string = string + "ing"

	print(string)