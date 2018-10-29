"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. 
But there are a few important conditions:
    The initial and final markers are always different.
    If there is no initial marker then the beginning should be considered as the beginning of a string.
    If there is no final marker then the ending should be considered as the ending of a string.
    If the initial and final markers are missing then simply return the whole string.
    If the final marker is standing in front of the initial one then return an empty string.
Example:
    between_markers('What is >apple<', '>', '<') == 'apple'
    between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
"""



def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    begin = text.find(begin) + len(begin) if begin in text else 0;
    end = text.find(end) if end in text else None
    print(begin,end)
    return text[begin:end]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')