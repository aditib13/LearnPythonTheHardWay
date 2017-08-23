def separate_words(response):
	words = response.split(' ')
	broken_words = []
	for i in words:
		broken_words.append(i)
	return broken_words

def categorize(word):
	categories = {
		"direction": ["north", "east", "south", "west", "down", "up", "right", "left", "back"]
		"verb": ["go", "stop", "kill", "eat"]
		"stop": ["the", "in", "of", "from", "at", "it"]
		"noun": ["door", "bear", "princess", "cabinet"]
	}

if word in categories:
	return categories