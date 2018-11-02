"""
you should find the length of the longest substring that consists of the same letter. 
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". 
The last substring is the longest one which makes it an answer.
Example:
	long_repeat('sdsffffse') == 4
	long_repeat('ddvvrwwwrggg') == 3
"""
from itertools import groupby

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    return max(len(list(g)) for k,g in groupby(line)) if line else 0

def long_repeat_v2(line):
    
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)

import re
def long_repeat_v3(line):
    """
        length the longest substring that consists of the same char
    """
    lyst = [len(i[0]) for i in re.findall(r'((\w)\2*)',line)]
    return max(lyst) if line else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')