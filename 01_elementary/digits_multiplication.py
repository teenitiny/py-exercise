"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
Example:
	checkio(123405) == 120
	checkio(999) == 729
	checkio(1000) == 1
	checkio(1111) == 1
"""

from functools import reduce
from operator import mul

def checkio(number: int) -> int:

    return reduce(mul,[int(i) for i in str(number) if i!='0'])


def checkio_v2(number: int) -> int:
	res = 1
	for i in str(number):
		res *= int(i) if int(i) else 1
	return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")