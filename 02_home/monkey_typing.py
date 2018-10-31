"""
You are given some text potentially including sensible words. 
You should count how many words are included in the given text. 
A word should be whole and may be a part of other word. Text letter case does not matter. 
Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once.
Example:
	count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
	count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
	count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
	            {"sum", "hamlet", "infinity", "anything"}) == 1
"""

def count_words(text: str, words: set) -> int:
    
    num = 0
    text = text.lower()
    for word in words:
        if word in text:
            num += 1
    return num

def count_words_v2(text, words):
    return sum(w in text.lower() for w in words)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
