"""
You are given a positive number as a string along with the radix for it. 
Your function should convert it into decimal form. The radix is less than 37 and greater than 1. 
The task uses digits and the letters A-Z for the strings.
Watch out for cases when the number cannot be converted. 
For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.
Example:
	checkio("AF", 16) == 175
	checkio("101", 2) == 5
	checkio("101", 5) == 26
	checkio("Z", 36) == 35
	checkio("AB", 10) == -1
"""

def checkio(str_number: str, radix: int) -> int:
    
    try:
        return int(str_number, radix)
    except ValueError:
        return -1


def checkio_v2(str_number, radix):
    wynik=0;
    k=len(str_number)-1
    abc="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    error=False
    for i in str_number:
        if abc.find(i)!=-1 and abc.find(i)<radix:
            liczba=abc.find(i)        
            wynik+=liczba*pow(radix,k)
            k-=1
        else: error=True
    if error : wynik=-1
    return wynik

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
