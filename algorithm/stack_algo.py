"""
Evaluating Postfix Expressions

Create a new stack
While there are more tokens in the expressioin
	Get the next token
	if the token is an operand
		Push the operand onto the stack
	Else if the token is an operator
		Pop the two operands from the stack
	Apply the operator to the two operands just opped
	Push the resulting value onto the stack
"""

"""
Converting Infix to Postfix

1. Start with an empty postfix expression and an empty stack, 
which will hold operators and left parentheses.
2. Scan across the infix expression from left to right.
3. On encountering an operand, append it to the postfix expression.
4. On encountering a left parenthesis, push it onto the stack.
5. On encountering an operator, pop off the stack all operator 
that have equal or higher precedence, append them to the postfix 
expression, and then push te scanned operator onto the stack
6. On encountering a right parenthesis, shift operators from the 
stack to the postfix expression until meeting the matching left
parenthesis, which is discarded.
7. On encountering the end of the infix expression, transfer the remaining operators from the stack to the postfix expression
"""

"""
BackTracking stack

Create an empty stack
Push the starting state onto the stack
While the stack is not empty
	Pop the stack and exmine the state
	if the state represents an ending state
		Return SUCCESSFUL CONCLUSION
	Else if the state has not been visited previously
		Mark the state as visited
		Push onto the stack all unvisited adjacent states
Return UNSUCCESSFUL CONCLUSION

Instantiate a stack
Locate the character "P" in the grid
Push its location onto the stack
While the stack is not empty
	Pop location. (row, colum), off the stack
	if the grid contains "T" at this location, then
		A path has been found
		Return True
	Else if this location does not contain a dot
		Place a dot in the grid at this location
		Examine the adjacent cells to this one and
		for each one that contains a space.
			push its location onto the stack
Return False
"""
