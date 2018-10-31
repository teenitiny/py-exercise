"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
Example:
	most_frequent([
	    'a', 'b', 'c', 
	    'a', 'b',
	    'a'
	]) == 'a'
	most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""

def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(data, key=data.count)

from statistics import mode as most_frequent_v2

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')