"""
In this mission you should check if all elements in the given list are equal.
Example:
	all_the_same([1, 1, 1]) == True
	all_the_same([1, 2, 1]) == False
	all_the_same(['a', 'a', 'a']) == True
	all_the_same([]) == True
"""

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    for e in elements[1:]:
        if e != elements[0]:
            return False
    return True

def all_the_same_v2(elements):

	return elements == elements[1:] + elements[:1]

def all_the_same_v3(elements: List[Any]) -> bool:

	return len(set(elements)) <= 1

def all_the_same_v4(elements):
    
    return all(elements[0] == e for e in elements[1:])

from itertools import groupby
def all_the_same_v5(elements):
    return sum(1 for _ in groupby(elements)) < 2

def all_the_same_v6(elements):
   return elements[1:] == elements[:-1]

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")