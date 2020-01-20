import re

def first_repeated(string):
	word_set = set()
	word_lst = re.findall(r'[A-Za-z]+\'?[a-z]*', string.lower())

	for word in word_lst:
		if word in word_set:
			return word
		else:
			word_set.add(word)

	return None