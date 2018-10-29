
"""
You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5; 
The number as a string for other cases.

Example:
    checkio(15) == "Fizz Buzz"
    checkio(6) == "Fizz"
    checkio(5) == "Buzz"
    checkio(7) == "7"
"""


def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.

    # replace this for solution
    d3 = (number % 3 == 0)
    d5 = (number % 5 == 0)
    if d3 and d5: return "Fizz Buzz"
    if d3: return "Fizz"
    if d5: return "Buzz"
    return str(number)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
