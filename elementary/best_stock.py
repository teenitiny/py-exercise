"""
You are given the current stock prices. You have to find out which stocks cost more.
Example:
    best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX'
    best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI'
"""

def best_stock(data):
    """
        return the market code have the max price
    """
    return max(data,key=lambda s:data[s])

def best_stock_v2(data):
    """
        return the market code have the max price
    """
    max_price = 0
    answer = ''
    for s in data:
        if data[s] > max_price:
            max_price = data[s]
            answer = s
    return answer

if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")