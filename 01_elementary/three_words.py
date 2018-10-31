"""
You are given a string with words and numbers separated by whitespaces (one space). 
The words contains only letters. You should check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains three words in succession.
Example:
	checkio("Hello World hello") == True
	checkio("He is 123 man") == False
	checkio("1 2 3 4") == False
	checkio("bla bla bla bla") == True
	checkio("Hi") == False
"""


import re

def checkio(words):
    return bool(re.search('\D+ \D+ \D+', words))


def checkio_v2(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))


def checkio_v3(words):
    succ = 0
    for word in words.split():
        if word.isalpha():
            succ += 1
            if succ == 3: return True
        else: succ = 0
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"