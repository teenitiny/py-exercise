"""
 develop a password security check module. 
 The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
 it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
 The password contains only ASCII latin letters or digits.
 Example:
	checkio('A1213pokl') == False
	checkio('bAse730onE') == True
	checkio('asasasasasasasaas') == False
	checkio('QWERTYqwerty') == False
	checkio('123456123456') == False
	checkio('QwErTy911poqqqq') == True
"""

def checkio(data: str) -> bool:

    #replace this for solution
    if len(data) < 10:
        return False
    if not any(i.isdigit() for i in data):
        return False
    if not any(i.isupper() for i in data):
        return False
    if not any(i.islower() for i in data):
        return False
    return True

#Some hints
#Just check all conditions

import re

DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')

def checkio_v2(data):

    if len(data) < 10:
        return False
    if not DIGIT_RE.search(data):
        return False
    if not UPPER_CASE_RE.search(data):
        return False
    if not LOWER_CASE_RE.search(data):
        return False
    return True

def checkio_v3(data):
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 10 else False

def checkio_v4(data):
    if len(data) < 10:
        return False
    if data.upper() == data:
        return False
    if data.lower() == data:
        return False
    return any(c.isdigit() for c in data)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")