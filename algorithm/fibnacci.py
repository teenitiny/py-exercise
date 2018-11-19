def fib(b):
	"""The recursive Fibonacci function."""
	if n < 3:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


from counter import Counter

def fib_linear(n, counter):
	"""Count the number of iterations in the Fibonacci
	function."""
	sum = 1
	first = 1
	second = 1
	count = 3
	while count <= n:
		counter.increment()
		sum = first + second
		first = second
		second = sum
		count += 1
	return sum