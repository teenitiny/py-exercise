"""
You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.
For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters, we get the message "HELLO".
Example:
	find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
	find_message("hello world!") == ""
"""

def find_message(text: str) -> str:
    """Find a secret message"""
    return "".join([c for c in text if c.isupper()])

find_message_v2 = lambda text: ''.join(filter(str.isupper, text))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")