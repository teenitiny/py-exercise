

def indexOfMin(lyst):
	"""Return the index of the minimum item."""
	minIndex = 0
	currentIndex = 1
	while currentIndex < len(lyst):
		if lyst[currentIndex] < lyst[minIndex]:
			minIndex = currentIndex
		currentIndex += 1
	return minIndex

def sequentialSearch(target, lyst):
	"""Returns the position of the target item if found.
	or -1 otherwise."""
	position = 0
	while position < len(lyst):
		if target == lyst[position]:
			return position
		position += 1
	return -1

def binarySearch(target, sortedLyst):
	left = 0
	right = len(sortedLyst) - 1
	while left <= right:
		midpoint = (left + right) // 2
		if target == sortedLyst[midpoint]:
			return midpoint
		elif target < sortedLyst[midpoint]:
			right = midpoint - 1
		else:
			left = midpoint + 1
	return -1

class SavingsAccount(object):
	"""This class represents a saving account
	with the owner's name, PIN, and balance."""
	def __init__(self, name, pin, balance=0.0):
		self._name = name
		self._pin = pin
		self._balance = balance

	def __lt__(self, other):
		return self._name < other._name
	# Other methods, including __eq__ .........


def swap(lyst, i, j):
	"""Exchange the items at positions i and j."""
	# You could say lyst[i], lyst[j] = lyst[j], lyst[i]
	# but the following code shows what is really going on
	temp = lyst[i]
	lyst[i] = lyst[j]
	lyst[j] = temp


def selectionSort(lyst):
	i = 0
	while i < len(lyst) - 1:
		minIndex = i
		j = i + 1
		while j < len(lyst):
			if lyst[j] < lyst[minIndex]:
				minIndex = j
			j += 1
		if minIndex != i:
			swap(lyst, minIndex, j)
		i += 1

def bubbleSort(lyst):
	n = len(lyst)
	while n > 1:
		i = 1
		while i < n:
			if lyst[i] < lyst[i-1]:
				swap(lyst, i, i-1)
			i += 1
		n -= 1

def bubbleSortWithTweak(lyst):
	n = len(lyst)
	while n > 1:
		swapped = False
		i = 1
		while i < n:
			if lyst[i] < lyst[i-1]:
				swap(lyst, i, i-1)
			i += 1
		n -= 1
		if not swapped: return
		n -= 1


def insertionSort(lyst):
	i = 1
	while i < len(lyst):
		itemToInsert = lyst[i]
		j = i - 1
		while j >= 0:
			if lyst[j] > itemToInsert:
				lyst[j+1] = lyst[j]
			j -= 1
		lyst[j+1] = itemToInsert
		i += 1
	
