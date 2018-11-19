"""
File: Stack
Author: Gang
"""

class ArrayStack:
	def __init__(self, lyst=None):
		self._item = list()
		if lyst:
			for i in lyst:
				self.push(i)

	def __iter__(self):
		for i in self._item:
			yield i

	def push(self, item):
		self._item.append(item)

	def pop(self):
		return self._item.pop()

	def peek(self):
		return self._item[-1]

	def __len__(self):
		return len(self._item)

	def __str__(self):
		result = ""
		for i in self:
			result += (str(i) + " ")
		return result

	def clear(self):
		self._item = []

	def isEmpty(self):
		return len(self) == 0

