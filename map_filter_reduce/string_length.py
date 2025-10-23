def get_string_length(word):
	return len(word)



strings = ["apple" , "banana" , "cherry"]
output = list(map(get_string_length , strings))

print(output)