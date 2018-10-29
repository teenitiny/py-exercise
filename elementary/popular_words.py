"""
In this mission your task is to determine the popularity of certain words in the text.
At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:
	The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
	The search words are always indicated in the lowercase.
	If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
Example:

	popular_words('''
	When I was One
	I had just begun
	When I was Two
	I was nearly new
	''', ['i', 'was', 'three', 'near']) == {
	    'i': 4,
	    'was': 3,
	    'three': 0,
	    'near': 0
	}

"""

def popular_words(text: str, words: list) -> dict:

    text = text.lower().split()
    popularity = {}
    for word in words:
        popularity[word]=text.count(word)
    return popularity

def popular_words_v2(text: str, words: list) -> dict:

	lower_count = text.lower().split().count
	return {word: lower_count(word) for word in words}

def popular_words_v3(text: str, words: list) -> dict:

	return dict(zip(words, map(text.lower().split.count, words)))


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")