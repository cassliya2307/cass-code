from functools import reduce

def concatinate_string(words , letter):
	return words + "-" + letter

words = ["I" , "Love", "Anime"]
output = reduce(concatinate_string , words)

print(output)