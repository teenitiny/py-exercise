"""
File: arrays.py
An Array is like a list, but the client can use
only[], len, iter, and str.
To instantiate, use
<variable> = Array(<capacity>, <optional fill value>)
The fill value is None by default.
"""

class Array(object):
	"""Represents an array."""
	def __init__(self, capacity=5, fillValue=None):
		"""Capacity is the static size of the array.
		fillValue is placed at each position."""

		self._items = list()
		for count in range(capacity):
			self._items.append(fillValue)

	def __len__(self):
		"""->The capacity of the array."""
		return len(self._items)

	def __iter__(self):
		"""Supports traversal with a for loop."""
		return iter(self._items)

	def __getitem__(self, index):
		"""Subscript operator for access at index."""
		return self._items[index]

	def __setitem__(self, index, newItem):
		"""Subscript operator for replacement at index."""
		self._items[index] = newItem

"""
DEFAULT_CAPACITY = 5
logicalSize = 0
a = Array(DEFAULT_CAPACITY)

if logicalSize == len(a):
	tem = Array(len(a) + 1)
	for i in range(logicalSize):
		temp[i] = a[i]
	a = temp

if logicalSize <= len(a) // 4 and len(a) >= DEFAULT_CAPACITY * 2:
	temp = Array(len(a) // 2)
	for i in range(logicalSize):
		temp[i] = a[i]
	a = temp

# Increase physical size of array if necessary

# Shift items down by one position

for i in range(logicalSize, targetIndex, -1):
	a[i] = a[i - 1]

# Add new item and increment logical size
a[targetIndex] = newItem
logicalSize += 1


# Shift items up by one position

for i in range(targetIndex, logicalSize - 1):
	a[i] = a[i + 1]

# Decrement logical size
logicalSize -= 1

# Decrease size of array if necessary
"""