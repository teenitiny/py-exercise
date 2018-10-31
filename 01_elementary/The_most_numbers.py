"""
You are given an array of numbers (floats). 
You should find the difference between the maximum and minimum element. 
Your function should be able to handle an undefined amount of arguments. 
For an empty argument list, the function should return 0.
Example:
	checkio(1, 2, 3) == 2
	checkio(5, -5) == 10
	checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
	checkio() == 0
"""


def checkio(*args):

    return max(args) - min(args) if args else 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")