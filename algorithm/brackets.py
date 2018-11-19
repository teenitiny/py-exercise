"""
File: brackets.py
Checks expressions for matching brackets
"""

from linkedstack import LinkedStack 

def bracketsBalance(exp):
	"""exp is a string that represents the expression"""
	stk = LinkedStack()
	for ch in exp:
		if ch in ['[','{','(']:
			stk.push(ch)
			print("pushes in", ch)
		elif ch in [']',')','}']:
			if stk.isEmpty():
				print("Stops at isEmpty")
				return False
			chFromStack = stk.pop()
			print("pops out", chFromStack)
			# Brackets must be of same type and match up
			if (ch == ']' and chFromStack != '[')\
			or (ch == '}' and chFromStack != '{')\
			or (ch == ')' and chFromStack != '('):
				print("Stops at test")
				return False
	return stk.isEmpty()

def main():
	exp = input("Enter a bracketd expression: ")
	if bracketsBalance(exp):
		print("OK")
	else:
		print("Not OK")


if __name__ == "__main__":
	main()