"""
Your mission here is to create a function that gets an tuple and returns a tuple with 3 elements 
- first, third and second to the last for the given array
Example:
	easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
	easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
	easy_unpack((6, 3, 7)) == (6, 7, 3)
"""

def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])


from operator import itemgetter
easy_unpack_v2 = itemgetter(0, 2, -2)

easy_unpack_3 = lambda e: (e[0], e[2], e[-2])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')