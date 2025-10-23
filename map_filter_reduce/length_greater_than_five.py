def remove_words_more_than_five_characters(words):
	if len(words) <= 5:
		return words



words = ["apple" , "kiwi", "banana" , "watermelon" , "fig" , "blueberry"]
output = list(filter(remove_words_more_than_five_characters,words))

print(output)