"""
You are given a text, which contains different english letters and punctuation symbols. 
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". 
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. 
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
example:
	checkio("Hello World!") == "l"
	checkio("How do you do?") == "o"
	checkio("One") == "e"
	checkio("Oops!") == "o"
	checkio("AAaooo!!!!") == "a"
	checkio("abe") == "a"
"""
import string

def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

from collections import Counter

def checkio_v2(text):
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")