
"""
You are given two strings and you have to find an index of the 
second occurrence of the second string in the first one.
Example:
    second_index("sims", "s") == 3
    second_index("find the river", "e") == 12
    second_index("hi", " ") is None
"""

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # str.index raise ValueError when it does not find the substring
    try:
        return text.index(symbol,text.index(symbol)+1)
    except ValueError:
        return None

def second_index_v2(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # enumerate allows us to loop over something and have an automatic counter, 
    # default start from zero
    count = 0
    for i, c in enumerate(text):
        if c == char:
            count += 1;
            if count == 2:
                return i
    return None

def second_index_v3(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # find returns -1 when is does not find the substring
    num = text.find(symbol, text.find(symbol)+1)
    return num if num>-1 else None

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')