from repeated_word import first_repeated
import pytest

string = 'The unreal is more powerful than the real. Because nothing is as perfect as you can imagine it. Because its only intangible ideas, concepts, beliefs, fantasies that last. Stone crumbles. Wood rots. People, well, they die. But things as fragile as a thought, a dream, a legend, they can go on and on. If you can change the way people think. The way they see themselves. The way they see the world. You can change the way people live their lives. That\'s the only lasting thing you can create.'

str2 = 'Happy birthday'

str3 = 'You are not your job, you\'re not how much money you have in the bank. You are not the car you drive. You\'re not the contents of your wallet. You are not your fucking khakis. You are all singing, all dancing crap of the world.'

def test_string_one():
	assert first_repeated(string) == 'the'

def test_string_two():
	assert first_repeated(str2) == None

def test_string_three():
	assert first_repeated(str3) == 'not'