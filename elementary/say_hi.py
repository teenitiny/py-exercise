"""
write a function that introduce a person with a given parameters in attributes.
	
Example:
	say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
	say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
"""

def say_hi(name: str, age: int) -> str:
    """
        Hi!
    """
    return "Hi. My name is %s and I'm %s years old" % (name, age)

if __name__ == '__main__':
	# use "asserts" for self checking 
    # assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    print(say_hi("Frank", 30))
    
