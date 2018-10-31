"""
You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
Example:
	checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
	checkio([1, 2, 3, 4, 5]) == []
	checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
	checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
"""
#Your optional code here
#You can import some modules or create additional functions
def checkio(data):
    result = []
    for item in data:
        if data.count(item) > 1:
            result.append(item)
    return result

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


def checkio_v2(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  
    start = 0
    while start < len(data):
        if data.count(data[start]) == 1: data.remove(data[start])
        else: start += 1
    return data

def checkio_v3(data):
        return [i for i in data if data.count(i) > 1]


from collections import Counter

def checkio_v4(data):
    counter = Counter(data)
    return [item for item in data if counter[item] > 1]

def checkio_v5(data):
    for item in data:
        if data.count(item) > 1:
            yield item

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")