"""
Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) 
using Caesar cipher(shift cipher) where each letter of input text is replaced by another that stands at a fixed distance. 
For example ("a b c", 3) == "d e f"
Example:
	to_encrypt("a b c", 3) == "d e f"
	to_encrypt("a b c", -3) == "x y z"
	to_encrypt("simple text", 16) == "iycfbu junj"
	to_encrypt("important text", 10) == "swzybdkxd dohd"
	to_encrypt("state secret", -13) == "fgngr frperg"
"""

from string import ascii_lowercase as lower

def to_encrypt(text, delta):
    #replace this for solution
    cipher = lower * 2
    delta = delta % 26 if delta >= 0 else (26 + delta) % 26
    new_text=''
    for c in text:
        if c.isalpha():
            new_text += cipher[cipher.index(c) + delta]
        else:
            new_text += c
    return new_text

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")